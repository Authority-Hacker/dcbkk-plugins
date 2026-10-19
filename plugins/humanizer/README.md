# Humanizer

Student-facing plugin for editing an existing draft to remove templated AI prose while preserving meaning, links, and the writer's own voice. It also supports a pattern-only audit; it does not certify AI authorship.

Use it with a pasted social post, email, reply, article excerpt, or documentation draft, or point it at a file. A voice sample is optional. It follows the sample first, then the draft's natural voice, then plain neutral prose. Ask for light or aggressive cleanup only when you want a different level of editing.

**Example:** “Humanize this email but keep the customer quote and URL exactly: [draft].” The result is the complete edited email and a brief note about consequential changes. A clean draft may come back unchanged. For files, the result is one final file per input, with source-to-output mapping; sibling variants remain separate.

The bundled Python 3 scanner is read-only and uses only the standard library. The skill calls it for suspected repetition, sibling variants, ambiguous mechanical tells, comprehensive audits, or exact punctuation work. Length alone does not require scanning. It can read file paths or pasted text on stdin. Its hits are candidates for editorial judgment, not automatic rewrite orders.

Complete documents are edited against their argument and voice, then compared directly with the original for omissions and changed qualifications. Follow-up requests revise the latest accepted result, retain earlier files, and deliver the complete revised file.

The editor compares the result with the source. It protects supported facts, direct quotes, links, citations, code, placeholders, headings, tables, and frontmatter unless asked to change them. A quoted dash stays intact when the request concerns editable prose. Detect-only requests return evidenced patterns without rewriting, AI probability, or an authorship claim.

Version `1.1.0` and plugin identity remain unchanged in this pilot. Historical 1.1 evaluation and review records describe earlier bytes; this candidate needs fresh outcome and installed-host evidence before any release review.
