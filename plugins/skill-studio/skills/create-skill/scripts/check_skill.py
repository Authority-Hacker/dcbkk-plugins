#!/usr/bin/env python3
"""Flag-only skill lint. Usage: check_skill.py <skill_dir> -> JSON.

Findings are data, not failures: only a missing/non-directory argument exits nonzero.
"""
import json
import pathlib
import re
import sys


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_KEY_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<key>[A-Za-z_][A-Za-z0-9_.-]*)[ \t]*:(?P<rest>.*)$")
FRONTMATTER_ITEM_RE = re.compile(r"^[ \t]+-[ \t]*(?P<item>.*)$")
BLOCK_HEADER_RE = re.compile(r"^(?P<style>[|>])(?P<chomp>[+-]?)(?P<indent>[0-9]*)[ \t]*(?:#.*)?$")
PERSONAL_PATH_RE = re.compile(r"(/Users/[^/\s\"']+/|/home/[^/\s\"']+/|C:\\Users\\[^\\\s\"']+\\)")

# Vendor-prefixed shapes only. A bare "40+ chars, mixed case, has a digit"
# matcher was dropped: it fired on ordinary product names and taglines, and
# because evidence is redacted before it is emitted the reader saw
# `[REDACTED]` and could not tell a leaked key from a headline.
SECRET_PATTERNS = [
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b"),
    re.compile(r"\bkey-[A-Za-z0-9_-]{24,}\b", re.I),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(
        r"\b(?:api[_-]?key|token|secret|password|passwd)\b\s*[:=]\s*([\"']?)([^\"'\s#]{8,})\1",
        re.I,
    ),
]
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PASSWORD_ASSIGN_RE = re.compile(r"\b(?:password|passwd)\b\s*[:=]\s*([\"']?)([^\"'\s#]{4,})\1", re.I)

# Executable-surface flags. A student's generated skill may carry a script; the
# deterministic layer should at least surface shell/network/env/config so the
# close can tell the person, in one plain line, what the skill can do.
# Flag-only, warn-level, model-interpreted — never blocks.
SCRIPT_EXTS = {".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".rb", ".pl", ".ps1"}
EXEC_SURFACE_PATTERNS = [
    ("shell_exec", "runs shell commands or deletes files — tell the person in one plain line what the skill can do",
     re.compile(r"\b(?:subprocess|os\.system|os\.popen|shutil\.rmtree|Popen)\b|\brm\s+-rf\b")),
    ("network_call", "makes network calls — tell the person in one plain line what the skill can reach",
     re.compile(r"\b(?:requests\.|urllib|http\.client|socket\.socket|fetch\()|\b(?:curl|wget)\s")),
    ("env_read", "reads environment variables, which may hold secrets — tell the person in one plain line what the skill can read",
     re.compile(r"\bos\.environ\b|\bgetenv\(|\bprocess\.env\b")),
]

# Frontmatter keys. Only name and description behave the same on Claude Code
# and Codex. The runtime keys below change behaviour on Claude Code only.
PORTABLE_FRONTMATTER_KEYS = {"name", "description"}
RUNTIME_FRONTMATTER_KEYS = {
    "allowed-tools", "disallowed-tools", "hooks", "model", "effort", "context",
    "agent", "background", "shell", "disable-model-invocation",
    "user-invocable", "paths", "arguments",
}
NAME_MAX_LENGTH = 64
CONFIG_SURFACE_NAMES = {"hooks.json", "settings.json", "settings.local.json", ".mcp.json"}

# Keep these names aligned with skill-safety-check's JUNK_BASENAMES and
# JUNK_DIRNAMES. The route is deliberately stricter than that scanner's
# severity: only disposable cache/desktop metadata is safe to remove without a
# checkpoint. Repositories, environment files, dependencies, build output,
# virtual environments, local configuration, logs, and other uncertain content
# may contain the only copy of something useful.
AUTO_REMOVE_JUNK_FILES = {".DS_Store", "Thumbs.db"}
AUTO_REMOVE_JUNK_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
CHECKPOINT_JUNK_FILES = {".python-version", "npm-debug.log", "yarn-error.log"}
CHECKPOINT_JUNK_DIRS = {
    ".git": "repository",
    "node_modules": "dependency directory",
    ".venv": "virtual environment",
    "venv": "virtual environment",
    "dist": "build output",
    "build": "build output",
    ".next": "build output",
    ".idea": "local configuration with uncertain contents",
    ".vscode": "local configuration with uncertain contents",
}


def _flag(flag_id, level, message, evidence=None, file=None, line=None):
    flag = {"id": flag_id, "level": level, "message": _sanitize_line(message)}
    if evidence:
        flag["evidence"] = _sanitize_line(str(evidence))
    if file:
        flag["file"] = _sanitize_line(str(file))
    if line:
        flag["line"] = line
    return flag


def _rel(path, root):
    return path.relative_to(root).as_posix()


def _looks_binary(path):
    try:
        with path.open("rb") as handle:
            chunk = handle.read(2048)
    except OSError:
        return True
    return b"\0" in chunk


def _read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def _text_files(root, flags):
    for path in sorted(root.rglob("*")):
        # Inventory links, never read through them. The caller must assess the
        # selected target separately within its authorization.
        if path.is_symlink():
            flags.append(_flag("unscanned_symlink", "info",
                               "symlink not followed; manual coverage required",
                               file=_rel(path, root)))
            continue
        if not path.is_file():
            continue
        if _looks_binary(path):
            flags.append(_flag("unscanned_file", "info",
                               "binary or unreadable file; manual coverage required",
                               file=_rel(path, root)))
            continue
        yield path


def _check_junk(root, flags):
    """Flag scanner-known junk and route deletion without deleting anything."""
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        # Once a whole directory is routed, its contents inherit that route.
        # Do not misleadingly mark a cache nested inside a checkpointed build or
        # repository as independently auto-removable.
        if any(
            part in AUTO_REMOVE_JUNK_DIRS or part in CHECKPOINT_JUNK_DIRS
            for part in relative.parts[:-1]
        ):
            continue
        rel = relative.as_posix()
        name = path.name

        if path.is_dir():
            if name in AUTO_REMOVE_JUNK_DIRS:
                flags.append(
                    _flag(
                        "junk_auto_remove",
                        "info",
                        "low-risk cache directory may be removed during a tidy pass",
                        evidence="cache directory; verify the exact target and rerun the checker",
                        file=rel,
                    )
                )
            elif name in CHECKPOINT_JUNK_DIRS:
                flags.append(
                    _flag(
                        "junk_checkpoint_required",
                        "warn",
                        "junk-like directory needs explicit approval before deletion",
                        evidence=CHECKPOINT_JUNK_DIRS[name],
                        file=rel,
                    )
                )
            continue

        if not path.is_file():
            continue
        if name in AUTO_REMOVE_JUNK_FILES:
            flags.append(
                _flag(
                    "junk_auto_remove",
                    "info",
                    "low-risk desktop metadata may be removed during a tidy pass",
                    evidence="disposable metadata; verify the exact target and rerun the checker",
                    file=rel,
                )
            )
        elif name.startswith(".env"):
            flags.append(
                _flag(
                    "junk_checkpoint_required",
                    "warn",
                    "environment file needs explicit approval before deletion",
                    evidence="environment files may contain configuration or secrets",
                    file=rel,
                )
            )
        elif name in CHECKPOINT_JUNK_FILES:
            flags.append(
                _flag(
                    "junk_checkpoint_required",
                    "warn",
                    "junk-like file needs explicit approval before deletion",
                    evidence="local configuration or log with uncertain contents",
                    file=rel,
                )
            )


def _sub_secret_value(match):
    if match.lastindex and match.lastindex >= 2:
        return match.group(0).replace(match.group(2), "[REDACTED]")
    return "[REDACTED]"


def _sanitize_line(line):
    """Redact every secret-like value on a line before it is EVER emitted as evidence.

    Used for all evidence strings, not only the secret flag: a personal-path or
    exec-surface flag can land on the same line as a key (a student pastes
    `api_key = "sk-..."  # /Users/<name>/keys.txt`), and no flag's evidence may
    reprint the key. Redacting here, at the single emission chokepoint, closes that.
    """
    redacted = line
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub(_sub_secret_value, redacted)
    redacted = PASSWORD_ASSIGN_RE.sub(
        lambda m: m.group(0).replace(m.group(2), "[REDACTED]"), redacted
    )
    return redacted


def _unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _strip_inline_comment(value, quote=None):
    """Drop a YAML inline comment: a `#` after whitespace and outside quotes.

    One quote-aware scan of the whole value. A quote opens only where a scalar
    starts (start of value, or after `[`, `,` or `{`), so an apostrophe inside a
    plain scalar is ordinary text; this also covers quoted flow-sequence
    elements. Single quotes escape with `''`, double quotes with a backslash.
    Returns (text, open_quote) so a multiline quoted scalar carries its quote
    state onto continuation lines and is never stripped mid-string.
    """
    out = []
    i = 0
    while i < len(value):
        ch = value[i]
        if quote:
            out.append(ch)
            if quote == '"' and ch == "\\" and i + 1 < len(value):
                out.append(value[i + 1])
                i += 2
                continue
            if ch == quote:
                if quote == "'" and value[i + 1:i + 2] == "'":
                    out.append("'")
                    i += 2
                    continue
                quote = None
            i += 1
            continue
        if ch == "#" and (i == 0 or value[i - 1] in " \t"):
            break
        if ch in "'\"":
            prev = "".join(out).rstrip()
            if not prev or prev[-1] in "[,{":
                quote = ch
        out.append(ch)
        i += 1
    text = "".join(out)
    return (text if quote else text.rstrip()), quote


def _dedent_block(raw_lines, explicit_indent):
    """Strip the block's own indentation, per YAML: the first non-empty line sets it."""
    if explicit_indent:
        width = int(explicit_indent)
    else:
        widths = [len(line) - len(line.lstrip()) for line in raw_lines if line.strip()]
        width = min(widths) if widths else 0
    return [line[width:] if len(line) >= width else line.lstrip() for line in raw_lines]


def _join_block(raw_lines, style, chomp, explicit_indent):
    """Collapse a `|` literal or `>` folded block into its string value."""
    body = _dedent_block(raw_lines, explicit_indent)
    if style == "|":
        text = "\n".join(body)
    else:
        # Folded: a run of non-empty lines joins with single spaces; each blank
        # line becomes one newline.
        parts, run = [], []
        for line in body:
            if line.strip():
                run.append(line.strip())
            else:
                parts.append(" ".join(run))
                run = []
                parts.append("\n")
        parts.append(" ".join(run))
        text = "".join(parts)
    if chomp == "+":
        return text
    return text.rstrip("\n")


def _parse_frontmatter(text):
    """Parse the YAML subset Claude Code skills actually use.

    Handles plain and quoted scalars, `>`/`|` block scalars (with chomping and
    explicit indent indicators), block sequences, and flow sequences. Anything
    outside that subset is reported once as unreadable — callers must not derive
    a second finding from a value this could not read.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "SKILL.md must start with frontmatter opening ---"

    close_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            close_index = index
            break
    if close_index is None:
        return {}, "SKILL.md frontmatter is missing closing ---"

    body = lines[1:close_index]
    data = {}
    errors = []
    index = 0
    while index < len(body):
        line = body[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue

        match = FRONTMATTER_KEY_RE.match(line)
        if not match or match.group("indent"):
            errors.append(f"line {index + 2}: {stripped}")
            index += 1
            continue

        key = match.group("key")
        rest = match.group("rest").strip()
        open_quote = None
        if not BLOCK_HEADER_RE.match(rest):
            rest, open_quote = _strip_inline_comment(rest)
        index += 1

        # A plain scalar may wrap onto following indented lines — which is what a
        # model writing an 80-column description produces. YAML folds those into
        # the value with single spaces; read them here rather than treating the
        # continuation as an unreadable line and the truncated first line as the
        # whole description.
        if rest and not BLOCK_HEADER_RE.match(rest) and not (rest.startswith("[") and rest.endswith("]")):
            while index < len(body) and body[index][:1] in " \t" and body[index].strip():
                if FRONTMATTER_ITEM_RE.match(body[index]):
                    break
                piece, open_quote = _strip_inline_comment(body[index].strip(), open_quote)
                rest += " " + piece
                index += 1

        block = BLOCK_HEADER_RE.match(rest) if rest else None
        if block:
            raw = []
            while index < len(body) and (not body[index].strip() or body[index][:1] in " \t"):
                raw.append(body[index])
                index += 1
            while raw and not raw[-1].strip():
                raw.pop()
            data[key] = _join_block(raw, block.group("style"), block.group("chomp"), block.group("indent"))
            continue

        if not rest:
            items = []
            while index < len(body):
                item = FRONTMATTER_ITEM_RE.match(body[index])
                if not item:
                    if body[index].strip():
                        break
                    index += 1
                    continue
                items.append(_unquote(item.group("item").strip()))
                index += 1
            data[key] = items if items else ""
            continue

        if rest.startswith("[") and rest.endswith("]"):
            data[key] = [_unquote(part.strip()) for part in rest[1:-1].split(",") if part.strip()]
            continue

        data[key] = _unquote(rest)

    if errors:
        return data, "frontmatter has lines this checker can't read (" + "; ".join(errors[:3]) + ")"
    return data, None


def _check_frontmatter(skill_md, skill_dir, flags):
    text = _read_text(skill_md)
    metadata, error = _parse_frontmatter(text)
    if error:
        # One informational flag, and nothing derived from it. A value this
        # parser could not read is unknown, not wrong — a "description too
        # short" invented on top of a parse failure once sent skills off to
        # have a perfectly good description rewritten.
        flags.append(_flag("frontmatter_unreadable", "info", error, file="SKILL.md"))

    for key in metadata:
        if key in PORTABLE_FRONTMATTER_KEYS:
            continue
        if key in RUNTIME_FRONTMATTER_KEYS:
            flags.append(_flag(
                "runtime_frontmatter_key", "warn",
                "changes how the skill runs on Claude Code only; mention it to the person and prefer leaving it out",
                evidence=key, file="SKILL.md"))
        else:
            flags.append(_flag(
                "unknown_frontmatter_key", "warn",
                "only name and description work the same on Claude Code and Codex; Codex ignores other settings",
                evidence=key, file="SKILL.md"))

    raw_name = metadata.get("name")
    raw_description = metadata.get("description")
    name = raw_name.strip() if isinstance(raw_name, str) else ""
    description = raw_description.strip() if isinstance(raw_description, str) else ""

    if not name:
        if not error and not isinstance(raw_name, list):
            flags.append(_flag("missing_name", "warn", "frontmatter is missing name", file="SKILL.md"))
    else:
        if not NAME_RE.match(name):
            flags.append(
                _flag("name_not_kebab_case", "warn", "name must be kebab-case", evidence=name, file="SKILL.md")
            )
        if len(name) > NAME_MAX_LENGTH and not error:
            flags.append(
                _flag("name_too_long", "warn", "name is over 64 characters, which Codex does not accept",
                      evidence=f"{len(name)} characters", file="SKILL.md")
            )
        if name != skill_dir.name:
            flags.append(
                _flag(
                    "name_dir_mismatch",
                    "warn",
                    "frontmatter name must match the skill directory name",
                    evidence=f"name={name}; dir={skill_dir.name}",
                    file="SKILL.md",
                )
            )

    if not description:
        if not error and not isinstance(raw_description, list):
            flags.append(
                _flag("missing_description", "warn", "frontmatter is missing description", file="SKILL.md")
            )
    elif error:
        # A description recovered from frontmatter this parser could not fully
        # read may be truncated. Length is not judgeable, so no length finding.
        pass
    elif len(description) < 60:
        flags.append(
            _flag(
                "description_too_short",
                "warn",
                "description is under 60 characters and may not trigger reliably",
                evidence=description,
                file="SKILL.md",
            )
        )
    elif len(description) > 1024:
        flags.append(
            _flag(
                "description_too_long",
                "warn",
                "description is over 1024 characters",
                evidence=f"{len(description)} characters",
                file="SKILL.md",
            )
        )

    if description and not error and ("<" in description or ">" in description):
        flags.append(
            _flag(
                "description_angle_brackets",
                "warn",
                "description contains < or >; some upload paths reject them in descriptions",
                evidence=description,
                file="SKILL.md",
            )
        )

    line_count = len(text.splitlines())
    if line_count > 400:
        flags.append(
            _flag("skill_md_too_large", "warn", "SKILL.md is over 400 lines", evidence=f"{line_count} lines", file="SKILL.md")
        )
    elif line_count > 150:
        flags.append(
            _flag("skill_md_long", "info", "SKILL.md is over 150 lines", evidence=f"{line_count} lines", file="SKILL.md")
        )


def _scan_text_file(path, root, flags):
    rel = _rel(path, root)
    is_script = path.suffix.lower() in SCRIPT_EXTS
    text = _read_text(path)
    for line_no, line in enumerate(text.splitlines(), start=1):
        for pattern in SECRET_PATTERNS:
            match = pattern.search(line)
            if not match:
                continue
            flags.append(
                _flag(
                    "possible_secret",
                    "warn",
                    "possible secret-like value found",
                    evidence=_sanitize_line(line).strip(),
                    file=rel,
                    line=line_no,
                )
            )
            break

        if EMAIL_RE.search(line) and PASSWORD_ASSIGN_RE.search(line):
            flags.append(
                _flag(
                    "email_password_pair",
                    "warn",
                    "email and password-like assignment found on the same line",
                    evidence=_sanitize_line(line).strip(),
                    file=rel,
                    line=line_no,
                )
            )

        path_match = PERSONAL_PATH_RE.search(line)
        if path_match:
            flags.append(
                _flag(
                    "absolute_personal_path",
                    "warn",
                    "absolute personal path found",
                    evidence=_sanitize_line(line).strip(),
                    file=rel,
                    line=line_no,
                )
            )

        if is_script:
            for surf_id, surf_msg, surf_re in EXEC_SURFACE_PATTERNS:
                if surf_re.search(line):
                    flags.append(
                        _flag(
                            surf_id,
                            "warn",
                            surf_msg,
                            evidence=_sanitize_line(line).strip(),
                            file=rel,
                            line=line_no,
                        )
                    )


def check_skill(skill_dir):
    skill_dir = pathlib.Path(skill_dir)
    flags = []
    checked_files = 0

    try:
        skill_md = skill_dir / "SKILL.md"
        if skill_md.is_file() and not skill_md.is_symlink():
            _check_frontmatter(skill_md, skill_dir, flags)
        else:
            flags.append(_flag("missing_skill_md", "warn", "skill directory is missing SKILL.md"))

        _check_junk(skill_dir, flags)

        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and (path.name in CONFIG_SURFACE_NAMES or path.parent.name == "hooks"):
                flags.append(
                    _flag(
                        "executable_config_present",
                        "warn",
                        "skill bundles a hooks/settings/MCP config that can change how Claude runs — tell the person in one plain line what it does",
                        evidence=_rel(path, skill_dir),
                    )
                )

        for path in _text_files(skill_dir, flags):
            checked_files += 1
            try:
                _scan_text_file(path, skill_dir, flags)
            except Exception as exc:  # fail open: one bad file is a flag, not a crash
                flags.append(
                    _flag(
                        "internal",
                        "info",
                        "internal checker error while scanning file",
                        evidence=f"{_rel(path, skill_dir)}: {type(exc).__name__}",
                    )
                )
    except Exception as exc:  # fail open: scanner bugs are data for the caller
        flags.append(
            _flag(
                "internal",
                "info",
                "internal checker error",
                evidence=f"{type(exc).__name__}: {exc}",
            )
        )

    return {"skill_dir": _sanitize_line(str(skill_dir)), "flags": flags, "checked_files": checked_files}


def main(argv):
    if len(argv) != 2:
        print(json.dumps({"error": "usage: check_skill.py <path-to-skill-dir>"}))
        return 2
    skill_dir = pathlib.Path(argv[1])
    if not skill_dir.is_dir():
        print(json.dumps({"error": "path is not a directory", "skill_dir": _sanitize_line(str(skill_dir))}))
        return 2
    print(json.dumps(check_skill(skill_dir), sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
