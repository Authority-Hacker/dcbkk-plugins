# Detect mode

Use this reference when the user wants an audit, scan, or opinion about AI-writing patterns without asking for a rewrite.

## Boundary

Detect observable writing patterns. Do not:

- Rewrite the draft.
- Assign a score, percentage, or probability that AI produced it.
- Guess which person, model, or tool wrote it.
- Treat polish, grammar, formatting, or one isolated phrase as proof.
- Invent findings to make the report feel useful.

If the user asks for proof of AI authorship, explain briefly that the skill can identify checkable patterns but cannot certify provenance. Continue with a pattern audit when that still answers the useful part of the request.

## Procedure

1. Identify the draft's surface and likely purpose when obvious.
2. Run the scanner for a long, repetitive, ambiguous, or comprehensive audit; otherwise read the text directly. Consult relevant sections of [`patterns.md`](patterns.md), or its full checklist for a comprehensive audit.
3. Group repeated instances of the same pattern.
4. Report only meaningful findings with direct evidence.
5. Stop before editing.

Use this shape:

| Pattern | Evidence | Why it reads mechanically | Fix direction |
|---|---|---|---|
| §N Name | Short exact quote | One sentence | A few words, not a rewrite |

If the text is clean, say `No meaningful patterns found.` You may name one or two borderline candidates as intentional choices, but do not pad the report.

For file jobs, save only the requested findings report. Keep it mapped to its input; do not create a rewrite or routine intermediate files.

## Completion gate

Before returning, confirm:

- Every finding names a catalog pattern and quotes the source.
- Repeated examples are grouped.
- No passage was rewritten.
- The report contains no AI-probability score or authorship claim.
