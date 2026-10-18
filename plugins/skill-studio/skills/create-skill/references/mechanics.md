# Mechanics

Most skills are plain instructions, and that is the default. Add a mechanic only when you can name the failure it fixes in this job ("one pass misses errors in a 40-row report"). When you add one, tell the person in one plain line what it adds and what it costs. Never offer this list as a menu.

## Loops

**Fixes:** a single pass that predictably falls short of the finish line, such as long pieces or strict formats. **In the skill:** "Draft, check it against What good looks like, revise. Stop after two rounds and say what still falls short." **Costs:** a longer run. **Skip it** when one pass already meets the bar. Always cap the rounds.

## Constraints

**Fixes:** output that drifts generic when the brief is open. **In the skill:** "Headline under 60 characters, one number, no adjectives: this audience trusts specifics." **Costs:** nothing. **Skip** limits the person didn't want; each one needs its reason.

## Release gates

**Fixes:** a known kind of mistake that slips through, such as the wrong client name or a missing affiliate disclosure. **In the skill:** "Before showing the draft, confirm the client name matches the brief and the disclosure sits in the first 100 words. Fix it rather than ask." **Costs:** seconds. **Skip** taste: gates check facts. Approval to spend or send was given when the skill was built, so a gate checks quality, not permission.

## Interactive pages

**Fixes:** choices that are painful in chat, such as comparing a dozen options, visual variants or approving a batch. **In the skill:** "Write the options to a local HTML page and open it. The person ticks their choices, and the page shows a short summary to paste back into the chat." The page can't send anything back by itself. **Costs:** one extra step for the person. **Skip it** for two or three options, which read fine in chat. A page with JavaScript is shipped code: open it and try it once before installing.

## Helper agents

Three uses:

- **Parallel workers** when the volume won't fit one thread: "Research each competitor in its own helper, then combine the notes."
- **Personas** that read a draft as its audience or a critic: "Have a helper read it as a busy CFO and list what they'd skip."
- **A fresh reviewer** with no stake in the draft, when self-checks keep missing the same thing.

**Costs:** more usage and a longer wait, so say so. **Fallback:** when the host can't start helpers, work in batches with notes saved between them, or for a review do a separate second pass in the same chat and say it isn't independent. **Skip them** for small jobs, or just to look thorough.

## Scripts

Most skills need none. A script earns its place only as one of these:

- **Flag:** points out things worth a look, and never decides.
- **Prebuild:** same-every-time mechanical work such as counting, sorting or removing duplicates. Good evidence for one: the test run rebuilt the same step by hand.
- **Rail:** stops before a real disaster, such as overwriting the person's data.

A script never judges voice, quality or what matters; that is the person's judgment and the assistant's job. If a script would need its own test campaign (several dependencies, side effects, a lot of logic), it is separate software: leave it out and say so. Run any script on the real input before installing. Prefer built-in language tools, and never write personal absolute paths.
