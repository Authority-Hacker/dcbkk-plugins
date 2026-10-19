---
user-invocable: false
name: create-skill
description: Use when turning a repeated task and the user's way of doing it into a skill for Claude Code or Codex, such as "make me a skill", "save how I do this" or "good, save that" after finished work. Works from a brief, examples or an accepted task, asks why where a reason matters, and tries the skill on real work before installing. For a task to do now while preferences are still forming, use skill-studio; for an existing skill's failure, preference change or rollback, use improve-skill; for a skill that has grown messy or contradictory, use tidy-skill.
---

# Create skill

Capture the person's way of doing a job in a skill that saves them re-explaining it, try it on real work, and install it where they choose. Before writing anything, clarify with them what a great result looks like. Match the effort to the skill: a few formatting rules should take minutes. Read [shared rules](references/run-policy.md) first.

## Start from what is known

If they want a task done now and are still working out how they like it ("help me with this, and remember how I like it"), follow [learn from work](../skill-studio/references/learn-from-work.md) first, and don't read this skill's references until they accept the work. A brief, examples or accepted work can start here directly.

Read the visible work before asking. Pull out the job, their rules and never-dos, voice and structure, the finish line, the scope, and which tools, connectors, files and sources the work used, in what order. Material they work from, such as transcripts, notes or data, is input, not an example: an example is a finished output they were happy with. Never invent one.

If they mention examples but haven't shared them, ask for those first. Then **run [clarify](references/clarify.md)** before drafting. Its questions go one at a time, each with your best guess and why, never as a list, until what's left wouldn't change the skill. Clear rules plus an example they like usually means no questions. There is no clear standard when there's no such example, or when the output has to perform (views, replies, sales) and nothing shows what success means. Then clarify goes deeper: the goal, the bar, great examples and the route.

Name the reuse benefit in one sentence. If nothing useful survives, say an ordinary prompt would do and stop.

## Ask why

Run [the why pass](references/interview-guide.md#the-why-pass): at most three questions built from their corrections and examples, only where knowing the reason would change future output. Zero is fine for a fixed format. When there was no clear standard, their reaction to the first trial gives the why pass its material.

## Size the effort

Most skills are a few rules about one kind of output: draft it, try it once on the real task, install it. Do more only where the skill needs it, and say what you'll do in one plain line ("This is a small one, so I'll write it and try it on your example"):

- **Several distinct cases** (different inputs or branches): try it on one real input per case. A lookup by client or brand name is one case.
- **A script or an interactive page:** run it on the real input before installing.
- **A copy of a plugin's skill:** follow [targets and forks](references/targets-and-forks.md).
- **No clear standard:** clarify in full, study the examples, agree the route, and get their reaction to the trial before installing.
- **They ask for thorough:** more real inputs.

If it will spend money or send, publish or delete things, get their yes now, as the shared rules describe. Create `~/.claude/skill-studio-work/<skill-name>/` with `run.md` and `draft/<skill-name>/`. On resume, read the notes and continue.

## Draft the smallest complete skill

Follow the [authoring rules](references/authoring-rules.md) and the [template](references/skill-template.md), including its self-update section. Most skills need only `SKILL.md`. Include every rule and never-do, with its reason where known, store useful excerpts, and write their finish line as the standard. Add a mechanic from [mechanics](references/mechanics.md) only when you can name the failure it fixes, and say in one line what it adds and what it costs them (more usage, a longer wait). Draft outside live skill folders.

## Try it

Run `scripts/check_skill.py` if Python is available; its output is flags, not decisions. Read the description against their own wording and the skills they already have. Then re-read the draft from disk and run it on the real task in the chat:

- Check the output against every rule and the finish line, pointing to where it meets each checkable one. Leave taste calls to them.
- Note any detour an instruction caused, and any step the run had to work out by hand. Reword or cut the instruction; a step rebuilt by hand is the evidence for a prebuild script.
- If the skill was learned from one example with specific names or figures, run it once more with those swapped, and check nothing from the example got baked in as a rule.

Fix what fails and recheck. If one correction doesn't fix it, say what's left. If there is no real task, say the first real use is the test.

## Install

Ask Personal or Project once, unless they already said. Ask it in the same message that shows the tried result, except when there was no clear standard: then wait for their reaction to the trial first, and if they asked for changes, show the revised result; "here", "this folder" or "this project" means Project. Creating a skill doesn't approve replacing another one: if a skill with that name exists, say so and back it up first ([backups](references/backups.md)). Install by replacing the folder whole, then re-read the installed files against the draft. If anything differs, stop, keep the backup and say so. A draft-only request finishes before this step.

## Close

In plain words:

- the skill's name and where it lives;
- one natural thing to say next time, and the fallback: "if it ever skips your rules, say the skill's name";
- what was tried and what wasn't. Whether it picks itself in a new chat is untried until it happens, so don't promise it;
- what it can touch, in one line, when it uses connectors, runs commands, spends or sends ("It uses your Gmail connector and sends to your team, as you agreed");
- that they can correct it as they go, and the way back if something was replaced.

If a new chat later misses it, improve-skill takes the actual prompt.
