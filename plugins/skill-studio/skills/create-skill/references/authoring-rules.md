# Authoring rules

You are writing a skill so a non-technical person's assistant does a repeated task their way, every time. These rules decide what good is.

## What a skill is for

A skill captures how this person does the job: their rules and the reasons behind them, their voice, their never-dos, their examples, and the tools and sources the work uses. The assistant then doesn't need it re-explained. Structure is only the container; a tidy file with none of their judgment is an empty box. If they don't have a way yet, the skill holds the route to a great result: the bar you agreed and the patterns from the examples you studied ([clarify](clarify.md)). Before writing, name the reuse benefit in one sentence: their judgment, instructions they would otherwise repeat, or a recurring format, source or tool routine. If there is none, an ordinary prompt will do.

## One skill, one job

A skill handles one job the person would name out loud ("write my product-roundup intros"). If part of it has different triggers or a different finish line, it is a separate skill.

## The description decides when it fires

Write it as a map of when to use it, not a summary of what it is.

- Lead with the situation and the input ("Use when…"), with the decisive words first: hosts shorten long descriptions.
- Add the phrases the person actually uses, plus one clause for how they ask without naming the task ("or when they paste a client brief and say 'do the usual'").
- Keep it specific enough to stay quiet at the wrong moment. No pressure wording such as "ALWAYS use".
- All trigger wording lives here. The body loads only after the skill is chosen, so trigger text there does nothing.
- Before finishing, read the descriptions of skills already installed for this person. If one overlaps, add a short boundary to the new one and suggest the matching edit to the other through improve-skill.
- Write in third person, never "I" or "we".

## Rules with reasons

Every instruction should be checkable and, where the person gave one, carry its reason:

- **Weak:** "handle the tone appropriately", "format as needed".
- **Strong:** "Never use exclamation points: the brand is understated." "Disclose affiliate links in the first 100 words: it's a legal requirement."

A reason lets the assistant handle the neighbouring case nobody listed. A plain rule with its reason works better than all-caps MUST or NEVER. When no reason is known, a plain rule is fine. Never-dos are the easiest judgment to lose, so capture them explicitly.

## Generalise, don't copy the example

The skill holds what carries over to the next task, not this week's facts. Client names, numbers, dates and one-off exceptions stay out unless they are the rule ("Acme always wants the budget line"). One correction is not automatically a permanent rule.

## Keep the main file lean

The main file loads on every run, so every line costs attention. Delete any line that doesn't change what the assistant does: "be thorough" changes nothing. Put long examples and edge cases in reference files, and make every link say when to read it: "Read the Acme file when the brief names Acme." Rules for different clients, brands or channels go in one file each, so one client's rules never bleed into another's output. Shorter is a result, not the goal: keep every line that carries judgment.

## Show, don't just tell

Where the judgment is subtle, as with voice and structure, a short real excerpt teaches more than adjectives. Store short excerpts of their own work in an examples file in the skill's references folder, and point at them. Never invent an example of their work.

## Plain instructions first

Most skills are plain instructions. Loops, gates, helper agents, interactive pages and scripts are described in [mechanics](mechanics.md); add one only when you can name the failure it fixes in this job.

## Let it keep learning

Write one rule per line under the heading it belongs to, so a later correction has an obvious place to go. The template's self-update section does the rest.

## Lead with the right words

The name, the headings and the first verb of each step should name the actual move ("draft", "check", "rewrite"). Precise words steer the assistant; filler doesn't.
