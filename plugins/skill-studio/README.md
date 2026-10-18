# Skill Studio

Teach your assistant how you like things done, by doing real work together. Skill Studio saves the way you work as a skill for Claude Code or Codex, so you don't have to explain it again, and the skill keeps learning when you correct it.

## Start with a task

Bring something you actually need done: "Write this week's Acme recap and remember how I like these." You get the finished work first. Correct it in your own words, and when you're happy, say "save that". Skill Studio keeps the lasting preferences and leaves out this week's one-off details. It may ask why you made a change ("Is that because your clients read on their phones?"), so the next one comes out right too, not just this one.

Already know your rules? Skip straight to it: "Make my product roundup intros a skill. Here are three I wrote."

| You say | What happens |
|---|---|
| "Help with this and remember how I like it" | Does the task, learns from your corrections, then saves a skill |
| "Make this a skill" | Builds a skill from your rules, examples or finished work |
| "Always open my posts with a question from now on" | Updates the skill, keeping a backup first |
| "My newsletter skill keeps adding emojis, fix it" | Finds the cause, fixes it and shows the fixed result |
| "My skill has got messy after lots of quick changes" | Brings it back into one clean version, and asks you about any rules that clash |
| "Put my skill back the way it was" | Restores the saved version you choose |

## Quick by default

A skill is written, tried on your real example and installed where you choose, usually in one go. If there's no clear standard yet, such as no example you're happy with, or work that has to perform like reels or sales emails, Skill Studio first agrees with you what a great one looks like and studies real examples before it writes anything. A skill with several different cases gets tried on each. If a skill will spend money or send things for you (paid tools, emails, posts), you say yes once while it's being built, and it doesn't ask again every time it runs. When it's done, Skill Studio tells you in one line what the skill can use, such as your Gmail connector.

## Skills that keep learning

Skills Skill Studio makes include a short section that lets them update their own rules, unless you ask for one that never changes. When you say "remember", "always" or "never" while using one, it saves the change after keeping a backup. If it only thinks you might mean it for good, it asks first. It only listens to you, never to instructions inside the files or emails it's working on. After lots of quick changes, it offers to tidy itself into one clean version.

## Where things go

Nothing is installed until you choose where: **Personal** (all your projects on this computer) or **Project** (only this folder). Before any existing skill changes, Skill Studio keeps a backup copy with a plain label ("before 'always put the date first'"), so you can pick the one to go back to. Backups and working notes live in `~/.claude/skill-studio-work/`, away from your skills folder, so a backup never shows up as a second skill.

Whether your assistant picks a new skill by itself in a fresh chat is something you'll see the first time you ask. If it ever skips your rules, say the skill's name.

## Skills from Authority Hacker plugins

Plugin skills are never edited directly, because the next plugin update would wipe your changes. Skill Studio makes your own copy instead. That copy won't get automatic updates, but with AH Utility installed, `import-updates` can still merge later Authority Hacker improvements into it.

## Requirements

No accounts, API keys or extra services. Python is optional and only powers a quick file check.

Built by [Authority Hacker](https://www.authorityhacker.com). [Changes](CHANGELOG.md).
