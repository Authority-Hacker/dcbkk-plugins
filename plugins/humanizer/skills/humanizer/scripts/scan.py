#!/usr/bin/env python3
"""Humanizer mechanical pre-scan.

Detects two kinds of AI-writing tell that have a reliable *surface form*:

  1. FIXED-SHAPE tells — exact characters, words, or phrases (em dashes, curly
     quotes, AI vocabulary, filler phrases, chatbot artifacts, etc.).
  2. TEMPLATE-SHAPE tells — recognizable syntactic rhythms, chiefly the
     antithesis/negative-parallelism family ("isn't X. It's Y", "you don't X.
     You Y", "Not X, just Y") and the "the real <noun>" authority trope. These
     read as semantic, but their *shape* is matchable, and they are the tells
     most likely to slip past a tired manual walk precisely because the writer
     reaches for them by reflex.

It still does NOT attempt the genuinely shape-free semantic patterns
(significance inflation, superficial -ing analyses, rule-of-three, false ranges,
diff-anchored writing, etc.); those need a human/model read and live in the
structured detection pass described in SKILL.md.

Why this exists: every invocation otherwise re-derives the regexes by hand and
drifts (misses the en dash one run, the antithesis rhythm the next). This script
makes the matchable part deterministic and gives verification a single gate.

It REPORTS, it never edits. A hit is a CANDIDATE, not a verdict — a lone curly
quote from a word processor, or a single earned contrast that carries the post's
whole point ("you don't need a better prompt. You need a gate."), is not an AI
tell. Apply the clustering rule in patterns.md ("Detection guidance") before
rewriting: an isolated template hit in otherwise human prose is kept; the same
template firing several times in one piece, or across a set of sibling posts, is
the reflex worth rewriting.

Canonical source for the vocabulary list is patterns.md §7. When you change the
wordlists or template regexes here, update the matching §-section in patterns.md
and the plugin README in the same change (see AGENTS.md, "The maintenance
contract").

Usage:
    python3 /path/to/loaded/skill/scripts/scan.py <file>
    python3 skills/humanizer/scripts/scan.py <file1> <file2> ...
        # set mode: also reports templates repeated across files
    python3 skills/humanizer/scripts/scan.py            # reads stdin
    cat draft.md | python3 skills/humanizer/scripts/scan.py

Set mode matters for sibling content (the X / LinkedIn / Threads variants of one
post): an antithesis used once is a choice, the same antithesis used in all three
variants is a crutch. Pass the related files together to surface that.

Exit code: 0 if no tells found, 1 if any found (so a verification step can gate
on it), 2 on usage/IO error.
"""

import re
import sys

# Fixed-shape phrase/word lists, keyed to the patterns.md section they detect.
# Each entry: section label -> list of case-insensitive phrases (matched as
# whole words / phrases via word boundaries).
PHRASE_TELLS = {
    "§4 promotional language": [
        "nestled", "vibrant", "breathtaking", "stunning", "must-visit",
        "renowned", "groundbreaking", "in the heart of",
    ],
    "§7 AI vocabulary": [
        "delve", "underscore", "underscores", "underscoring", "testament",
        "tapestry", "showcase", "showcases", "showcasing", "interplay",
        "intricate", "intricacies", "pivotal", "enduring", "garner", "garners",
        "leverage", "leveraging", "seamless", "seamlessly", "realm",
    ],
    "§8 copula avoidance": [
        "serves as", "serve as", "stands as", "stand as", "boasts a",
        "boasts an", "features a", "is a testament", "stands as a testament",
    ],
    "§9 negative parallelism": [
        "it's not just", "it is not just", "not just about", "not only",
        "not merely", "no guessing", "no wasted",
    ],
    "§20 chatbot artifacts": [
        "i hope this helps", "let me know if", "here is a", "here is an",
        "of course!", "certainly!", "would you like me to", "feel free to",
    ],
    "§21 cutoff / gap-filling": [
        "as of my last", "up to my last training", "while specific details are limited",
        "while specific details are scarce", "based on available information",
        "not publicly available", "maintains a low profile",
        "keeps personal details private", "prefers to stay out of the spotlight",
    ],
    "§22 sycophantic tone": [
        "great question", "you're absolutely right", "you are absolutely right",
        "excellent point", "happy to help", "that's a great",
    ],
    "§23 filler phrases": [
        "in order to", "due to the fact that", "at this point in time",
        "in the event that", "has the ability to", "have the ability to",
        "it is important to note", "it's important to note", "needless to say",
    ],
    "§24 excessive hedging": [
        "could potentially", "potentially possibly", "might possibly",
        "may potentially", "it could be argued that",
    ],
    "§25 generic / recap conclusions": [
        "the future looks bright", "exciting times lie ahead",
        "journey toward excellence", "step in the right direction",
        "the possibilities are endless", "in conclusion", "in summary",
        "to sum up",
    ],
    "§26 hyphenated word pairs": [
        "cross-functional", "data-driven", "client-facing", "decision-making",
        "real-time", "end-to-end", "high-quality", "long-term", "well-known",
        "cutting-edge", "state-of-the-art",
    ],
    "§27 authority tropes": [
        "the real question is", "at its core", "what really matters",
        "the heart of the matter", "the deeper issue", "fundamentally,",
        "in reality,", "what most people get wrong", "here's what nobody tells you",
        "the part everyone misses",
    ],
    "§28 signposting / rhetorical setups": [
        "let's dive in", "lets dive in", "let's explore", "let's break this down",
        "here's what you need to know", "without further ado", "now let's look at",
        "buckle up", "what if i told you", "think about it", "plot twist",
    ],
}


def _phrase_regex(phrase):
    """Return a unicode-aware boundary regex for a fixed tell phrase."""
    parts = re.split(r"\s+", phrase.strip())
    body = r"\s+".join(re.escape(part) for part in parts)
    prefix = r"(?<![^\W_])" if phrase[:1].isalnum() else ""
    suffix = r"(?![^\W_])" if phrase[-1:].isalnum() else ""
    return re.compile(prefix + body + suffix, re.IGNORECASE)


PHRASE_PATTERNS = {
    section: [(phrase, _phrase_regex(phrase)) for phrase in phrases]
    for section, phrases in PHRASE_TELLS.items()
}

# --- Template-shape tells -------------------------------------------------
#
# The antithesis family (§9) and the "real <noun>" trope (§27) are not fixed
# phrases, but their *rhythm* is matchable. Each regex targets one reflex
# construction. These fire per-sentence; the report groups them and the
# clustering rule (in patterns.md) decides what to actually rewrite. The point
# is to make the rhythm visible, not to auto-condemn it — one earned contrast is
# human, the same beat three times is the tell.
#
# Patterns are deliberately conservative: they look for the negation + pivot
# rhythm, not every "not" in the text. Each is documented with the shape it
# catches.
TEMPLATE_TELLS = [
    # "It's not X, it's Y" / "isn't X. It's Y" — the classic two-beat
    # antithesis. The reliable tell is that the SECOND beat re-asserts with a
    # back-referential pronoun (It's / That's / They're) pointing at the same
    # subject. We deliberately do NOT accept a bare "you/we/the" opener as the
    # second beat: "...because it isn't exciting. You could run 50" is just the
    # next sentence, not an antithesis, and matching it produced false hits.
    (
        "§9 negative parallelism",
        "isn't/not-X, it's-Y antithesis",
        re.compile(
            r"\b(?:it|that|this|the\s+\w+)?\s*"
            r"(?:is\s?n't|are\s?n't|was\s?n't|were\s?n't|'s\s+not|s\s+not|"
            r"is\s+not|are\s+not|was\s+not|were\s+not|isn't|aren't|wasn't|weren't)\b"
            r"[^.!?]{1,80}?[.,;]\s*"
            r"(?:it'?s|its|they'?re|that'?s|this'?s|he'?s|she'?s|"
            r"it\s+is|that\s+is|this\s+is|they\s+are)\b",
            re.IGNORECASE,
        ),
    ),
    # "You don't X. You Y" / "You don't X, you Y" — the imperative antithesis.
    (
        "§9 negative parallelism",
        "you-don't-X, you-Y antithesis",
        re.compile(
            r"\byou\s+(?:do\s?n't|don't|aren't|can't|won't)\b[^.!?]{1,80}?[.,;]\s*you\b",
            re.IGNORECASE,
        ),
    ),
    # "Not X, just Y" / "Not X. Just Y" as a sentence opener or
    # tail — the clipped negation pivot ("Not prompting harder, just leaving
    # better notes.").
    (
        "§9 negative parallelism",
        "Not-X, just/merely-Y clipped pivot",
        re.compile(
            r"(?:^|[.!?]\s+)not\s+[^.!?]{1,60}?[,.]\s*(?:just|merely|simply|only)\b",
            re.IGNORECASE,
        ),
    ),
    # "The real <noun> is" / "That's the real <noun>" — authority trope that
    # claims to cut to the essence (§27).
    (
        "§27 authority tropes",
        "the-real-<noun> framing",
        re.compile(
            r"\bthe\s+real\s+(?:question|skill|problem|issue|reason|story|"
            r"work|fix|answer|point|difference)\b",
            re.IGNORECASE,
        ),
    ),
    # "It's not about X, it's about Y" — the about-pivot variant, very common in
    # LinkedIn-voice copy.
    (
        "§9 negative parallelism",
        "not-about-X, about-Y pivot",
        re.compile(
            r"\bnot\s+(?:just\s+)?about\b[^.!?]{1,80}?[,.;]\s*(?:it'?s|its)\s+about\b",
            re.IGNORECASE,
        ),
    ),
    (
        "§31 colon reveals",
        "dramatic colon reveal",
        re.compile(
            r"(?i:\b(?:"
            r"(?:the\s+)?(?:best|worst|hardest|easiest)\s+(?:part|thing)"
            r"|(?:the\s+)?detail\s+that\s+makes?\s+it\s+work"
            r")\s*):\s*[a-z]",
        ),
    ),
]

TEMPLATE_LABELS = {(section, label) for section, label, _rx in TEMPLATE_TELLS}


def _blank_protected(line):
    """Replace protected content with spaces, preserving newline bytes."""
    return "".join(ch if ch in "\r\n" else " " for ch in line)


INLINE_CODE_RE = re.compile(r"`+[^`\n]*`+")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


def mask_protected_regions(text):
    """Blank code fences, inline code, and YAML frontmatter without moving lines."""
    lines = text.splitlines(keepends=True)
    masked = []
    # Only treat a leading --- as frontmatter if a closing delimiter exists
    # nearby; otherwise it's a Markdown thematic break and masking it would
    # swallow the whole document.
    in_frontmatter = bool(
        lines
        and lines[0].strip() == "---"
        and any(ln.strip() in ("---", "...") for ln in lines[1:30])
    )
    in_fence = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter:
            masked.append(_blank_protected(line))
            if i > 0 and stripped in ("---", "..."):
                in_frontmatter = False
            continue

        fence = FENCE_RE.match(line)
        if in_fence:
            masked.append(_blank_protected(line))
            if fence and fence.group(1).startswith(in_fence):
                in_fence = None
            continue
        if fence:
            in_fence = fence.group(1)[:3]
            masked.append(_blank_protected(line))
            continue

        masked.append(INLINE_CODE_RE.sub(lambda m: " " * len(m.group()), line))

    return "".join(masked)


def _normalize_template_text(text):
    return text.replace("’", "'").replace("‘", "'")


def iter_paragraphs(lines):
    """Yield (start_lineno, paragraph_text) for blank-line separated paragraphs."""
    start = None
    parts = []
    for i, line in enumerate(lines, 1):
        if line.strip():
            if start is None:
                start = i
            parts.append(line.strip())
            continue
        if parts:
            yield start, " ".join(parts)
            start = None
            parts = []
    if parts:
        yield start, " ".join(parts)


def find_template_hits(lines):
    """Return {section: [(lineno, sample, text), ...]} for template-shape tells.

    These are the antithesis/authority rhythms that read as 'semantic' but have
    a matchable surface form. Reported as candidates; clustering decides.
    """
    hits = {}
    for i, paragraph in iter_paragraphs(lines):
        normalized = _normalize_template_text(paragraph)
        for section, label, rx in TEMPLATE_TELLS:
            for _m in rx.finditer(normalized):
                hits.setdefault(section, []).append((i, label, paragraph.strip()))
    return hits


# Emoji ranges (common pictographic blocks). Deliberately broad but excludes
# plain punctuation and ASCII.
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"  # symbols & pictographs, supplemental, extended-A
    "\U00002600-\U000027BF"  # misc symbols + dingbats
    "\U0001F000-\U0001F0FF"  # mahjong/dominoes/cards
    "\U00002B00-\U00002BFF"  # arrows/stars (★ etc. used as bullets)
    "\U0001F1E6-\U0001F1FF"  # regional indicators (flags)
    "]"
)

CURLY_QUOTES = "‘’“”"  # ' ' " "
CURLY_RE = re.compile("[" + CURLY_QUOTES + "]")

# em dash, en dash; plus spaced em dash, spaced hyphen, and tight word--word.
DASH_RE = re.compile(r"—|–|\s--\s|\s-\s|(?<=[^\W\d_])--(?=[^\W\d_])")
FILENAME_LINE_RE = re.compile(r"^\S+\.[A-Za-z0-9]{1,8}$")

BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*")
INLINE_HEADER_RE = re.compile(
    r"^\s*(?:[-*]|\d+[.)])\s+"
    r"(?:\*\*[^*\n]+:\*\*|\*\*[^*\n]+\*\*:|__[^_\n]+:__|__[^_\n]+__:)"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")

# Words that don't count toward "Title Case" (articles/conjunctions/prepositions).
SMALL_WORDS = {
    "a", "an", "the", "and", "or", "but", "nor", "for", "so", "yet", "of",
    "to", "in", "on", "at", "by", "as", "is", "vs", "via", "with", "from",
}


def find_phrase_hits(lines):
    """Return {section: [(lineno, phrase, text), ...]} for phrase/word tells."""
    hits = {}
    for section, phrases in PHRASE_PATTERNS.items():
        for i, line in enumerate(lines, 1):
            for phrase, rx in phrases:
                if rx.search(line):
                    hits.setdefault(section, []).append((i, phrase, line.strip()))
    return hits


def find_regex_hits(lines):
    """Return {section: [(lineno, sample, text), ...]} for char/structure tells."""
    hits = {}

    def add(section, lineno, sample, text):
        hits.setdefault(section, []).append((lineno, sample, text))

    bold_lines = []
    for i, line in enumerate(lines, 1):
        for m in DASH_RE.finditer(line):
            if m.group() == "--" and FILENAME_LINE_RE.match(line.strip()):
                continue
            add("§14 em/en dashes", i, repr(m.group()), line.strip())
        for m in CURLY_RE.finditer(line):
            add("§19 curly quotes", i, m.group(), line.strip())
        for m in EMOJI_RE.finditer(line):
            add("§18 emojis", i, m.group(), line.strip())
        if INLINE_HEADER_RE.search(line):
            add("§16 inline-header lists", i, "- **Header:**", line.strip())
        if BOLD_RE.search(line):
            bold_lines.append((i, line.strip()))
        hm = HEADING_RE.match(line)
        if hm:
            heading = hm.group(2)
            words = [w for w in re.findall(r"[A-Za-z][\w']*", heading)]
            capd = [w for w in words if w[0].isupper()]
            # Title Case = most non-small words capitalized AND at least one
            # small word that should have been lowercase is capitalized,
            # or 3+ capitalized words beyond the first.
            capd_small = [w for w in words[1:]
                          if w.lower() in SMALL_WORDS and w[0].isupper()]
            if len(words) >= 3 and (capd_small or len(capd) >= 3 and len(capd) == len(words)):
                add("§17 title case headings", i, heading, line.strip())

        # Conservative candidate for the repeated punchline rhythm in social copy.
        sentences = [
            sentence.strip()
            for sentence in re.split(r"(?<=[.!?])\s+", line.strip())
            if sentence.strip()
        ]
        short_run = []
        for sentence in sentences:
            word_count = len(re.findall(r"\b[\w']+\b", sentence))
            if sentence.endswith(".") and 1 <= word_count <= 4:
                short_run.append(sentence)
                if len(short_run) == 3:
                    add("§32 robotic rhythm", i, "three short sentences", " ".join(short_run))
            else:
                short_run = []

    # Boldface only counts as a tell when it clusters (mechanical heuristic:
    # 3+ bold spans across the document). A single bold phrase is fine.
    total_bold = sum(len(BOLD_RE.findall(l)) for l in lines)
    if total_bold >= 3:
        for i, text in bold_lines:
            add("§15 boldface overuse", i, "**...**", text)

    return hits


def scan_text(text):
    """Run all three detectors on one document. Returns {section: [hits]}."""
    lines = mask_protected_regions(text).splitlines()
    hits = {}
    for d in (find_regex_hits(lines), find_phrase_hits(lines),
              find_template_hits(lines)):
        for section, items in d.items():
            hits.setdefault(section, []).extend(items)
    return hits


def report_hits(hits, header_label):
    """Print one document's hit report. Returns True if any hits."""
    if not hits:
        print(f"{header_label}No mechanical tells found. Review meaning and voice in context.")
        return False

    total = sum(len(v) for v in hits.values())
    print(f"{header_label}{total} candidate hit(s) across {len(hits)} pattern(s).")
    print("These are candidates, not verdicts. Keep earned choices and protected text; "
          "rewrite reflexive or repeated shapes when they hurt the draft.\n")
    for section in sorted(hits, key=lambda s: int(re.match(r"§(\d+)", s).group(1))):
        items = hits[section]
        print(f"{section}  ({len(items)} hit{'s' if len(items) != 1 else ''})")
        seen = set()
        for lineno, sample, text in items:
            key = (lineno, sample)
            if key in seen:
                continue
            seen.add(key)
            quote = text if len(text) <= 100 else text[:97] + "..."
            print(f"  line {lineno}: {sample}  | {quote}")
        print()
    return True


def report_cross_file(per_file_hits):
    """Surface template tells that repeat across sibling files.

    The loudest tell in a content set is the SAME reflex in every variant: an
    antithesis used once is a choice, used in all three platform variants it's a
    crutch. This pass exists because a per-file scan can call each variant
    'clean enough' while the repetition across them is glaring.
    """
    # Collect template-section hits by their label, tracking which files used each.
    by_label = {}
    for fname, hits in per_file_hits.items():
        labels_in_file = set()
        for section, items in hits.items():
            if section not in (
                "§9 negative parallelism", "§27 authority tropes",
                "§31 colon reveals", "§32 robotic rhythm",
            ):
                continue
            for _lineno, label, _text in items:
                if section != "§32 robotic rhythm" and (section, label) not in TEMPLATE_LABELS:
                    continue
                group = "template-shape rhythm" if section in (
                    "§9 negative parallelism", "§27 authority tropes"
                ) else label
                labels_in_file.add((section, group))
        for key in labels_in_file:
            by_label.setdefault(key, []).append(fname)

    repeated = {k: v for k, v in by_label.items() if len(v) >= 2}
    if not repeated:
        return False

    print("=" * 60)
    print("CROSS-FILE REPETITION — same template rhythm in multiple files.")
    print("The strongest rewrite signal: a beat used once is a choice, the same")
    print("beat across sibling variants is a reflex. Vary or cut all but one.\n")
    for (section, label), files in sorted(repeated.items(), key=lambda kv: -len(kv[1])):
        print(f"{section} / {label}  — in {len(files)} files:")
        for f in files:
            print(f"    {f}")
        print()
    return True


def main(argv):
    paths = argv[1:]
    try:
        if not paths:
            docs = {"<stdin>": sys.stdin.read()}
        else:
            docs = {}
            for p in paths:
                with open(p, "r", encoding="utf-8") as fh:
                    docs[p] = fh.read()
    except OSError as exc:
        sys.stderr.write(f"scan.py: cannot read input: {exc}\n")
        return 2

    multi = len(docs) > 1
    any_hits = False
    per_file_hits = {}
    for name, text in docs.items():
        hits = scan_text(text)
        per_file_hits[name] = hits
        label = f"[{name}] " if multi else ""
        if multi:
            print(f"===== {name} =====")
        if report_hits(hits, label):
            any_hits = True
        if multi:
            print()

    if multi:
        if report_cross_file(per_file_hits):
            any_hits = True

    return 1 if any_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
