---
name: improve-skill
description: Use when an existing skill or taught workflow gives wrong output, misses rules, loses voice, fails to trigger, needs a lasting preference changed, or needs rollback, such as "fix my skill", "always do X from now on" or "put it back". Small preference changes get a quick backed-up edit; real failures get the smallest repair, proved on the input that failed. New skills belong to create-skill; a skill that has grown messy or contradictory belongs to tidy-skill; one-off output edits do not belong here.
---

# Improve skill

Fix the exact complaint while keeping the person's judgment. A plausible edit plus "try it next time" is not a fix.

Read [shared rules](../create-skill/references/run-policy.md). Find the exact skill in the host's personal, project or plugin skills; if two share a name, settle which one before writing. Read the whole skill. If it holds a secret, say which file and offer to move it out. A plugin's skill takes the copy route in [targets and forks](../create-skill/references/targets-and-forks.md) first.

## Preference change

A lasting rule for the skill's existing job ("always put the meeting date first", "stop adding emojis", "Acme wants the budget line every time") is a small edit:

1. Back it up ([backups](../create-skill/references/backups.md)).
2. Widen or reword an existing rule if one covers it; otherwise add one, in their words, with their reason if they gave one. Keep one-off exceptions out.
3. Re-read the skill and run it on the input just corrected, usually already in the chat, and show the result. If it doesn't produce the corrected result, treat it as a repair.
4. Say what changed in one sentence, and that they can ask to put it back.

## Put it back

Follow [backups](../create-skill/references/backups.md#putting-it-back): list the saves by their labels, save the current version, replace the whole folder, re-read. If they already said which version, don't ask again. If nothing was saved, say nothing changed. Restoring is the whole job; don't start improving after it.

## Repair

Use the input and bad output they supplied, and ask only for what's missing. For "it never runs", their wording plus the skill not being picked is the failure.

Link the failure to a cause: a specific instruction, a missing rule, a description gap or a script. A vague "it's off" or a checker flag alone isn't a cause. A brand-new job routes to create-skill. If the cause is many stacked or clashing rules rather than one, fix the complaint, then offer a tidy.

Back the skill up, then make the smallest repair on a copy outside the live folder. New rules carry their reason; widen an existing rule before adding one. Re-read the copy and run the exact input that failed, then anything else the change touches, and show the outputs. A different nice example doesn't close the complaint. If the repair changes what the skill spends or who it reaches, get their yes first. If it meets what they asked for, say so; ask one focused question only if a taste call is still open.

For trigger complaints, fix the description, then say it stays untried until a new chat, and give the fallback: "if it ever skips your rules, say the skill's name." Don't turn a plugin off or rename a copy as a routing fix.

Replace the live folder with the repaired copy as a whole and re-read it. Close with what changed, the before and after on the failing input, and how to put it back. If the replacement fails, restore the backup and say so.
