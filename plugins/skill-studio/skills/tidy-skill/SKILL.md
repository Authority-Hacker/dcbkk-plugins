---
user-invocable: false
name: tidy-skill
description: Use when a skill has picked up lots of quick edits and become long, repetitive or contradictory, or the person asks to tidy, simplify or clean it up. Rebuilds it into one coherent, leaner version that keeps every rule's effect and asks about clashing rules. Wrong output on a specific task or a single preference change belongs to improve-skill; a new job belongs to create-skill; ordinary documents are excluded.
---

# Tidy skill

Skills drift as quick corrections pile up: rules stack, repeat and contradict, and the skill loses its shape. Bring it back into one clean, coherent version that keeps every rule's effect. Leaner is the result; keeping what it does is the point.

Read [shared rules](../create-skill/references/run-policy.md). Find the exact skill and read every file. A specific wrong output or a single new preference goes to improve-skill; a new job goes to create-skill. A plugin's skill takes the copy route in [targets and forks](../create-skill/references/targets-and-forks.md) first. Back it up ([backups](../create-skill/references/backups.md)) and say the original can come back.

## 1. Recover the vision

From the skill, its backup labels and the chat, write three or four plain lines: what it's for, who it's for, and what good looks like. Show them and let the person correct them. Every cut is judged against these lines.

## 2. List every rule

Pull out each rule as one line, with where it lives and its reason if known. Mark each one as [tidy rules](references/tidy-rules.md) describes: keep, duplicate, stacked, clashing, fights the vision, or changes nothing.

## 3. Settle clashes with the person

Ask about clashing rules, and rules that fight the vision: at most three questions, one at a time, using the backup labels for history ("On 3 Oct you added 'no emojis', on 12 Oct 'one emoji in headlines'. Which stands?"). Never pick silently.

## 4. Rewrite from the list

Write the skill fresh in the shape of create-skill's [template](../create-skill/references/skill-template.md): what it needs, how to do it, never-dos with reasons, what good looks like, examples in references, and the self-update section. Merge stacked rules into one broader rule with its reason. Keep the person's own wording for voice rules, steering phrases and stored examples. Change the description only if they agree.

## 5. Account for every rule

Check every rule on the list against the new version: where it now lives, "merged into…", "cut: changed nothing", or "settled by you". Anything unaccounted for goes back in. Keep this list in the notes.

## 6. Offer a real-run check

Offer it in one line: "Want me to run the old and new versions on a real example to compare? It takes a minute and catches voice drift." If they say yes, use a real input from the chat or the stored examples, and run each version separately, in helpers when available so neither sees the other. Compare the outputs against the rule list, voice included. Fix what slipped and say what you changed.

## 7. Replace and close

Replace the live folder with the new version as a whole and re-read it. Add a "tidied into one clean version" line to the backup index, so the count of quick changes starts again. Close with the vision lines, the line count before and after, what merged, what was cut, what they settled, and that they can ask to put the original back.
