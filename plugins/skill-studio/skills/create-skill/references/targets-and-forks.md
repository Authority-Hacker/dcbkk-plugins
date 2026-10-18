# Where skills go, and copies of plugin skills

## Personal or Project

**Personal** is the host's personal skills folder: every project on this computer. **Project** is this project's skills folder: only here. Claude Code and Codex keep these in different places, so use the folders of the host the person is using now.

## Copying a plugin's skill

Never edit a skill that came with a plugin: the next plugin update replaces it and their changes are lost. Make a personal copy instead. Explain the trade-off once, that the copy stops getting automatic updates, and ask unless they already accepted it.

- First check the destination. If a personal skill with that name already exists, it may be an earlier copy they customised: back it up ([backups](backups.md)) and ask whether to replace it, before copying anything there.
- Copy the whole skill folder and keep its name. AH Utility's `import-updates` finds a copy by its name, so renaming it would cut it off from later Authority Hacker improvements.
- While the original is still on, either version may answer. If they don't need the plugin's other skills, offer to turn the plugin off, and say that silences all of them. Don't turn it off without a yes, and don't rename the copy to dodge the overlap.
- For an Authority Hacker skill, when `import-updates` is available, run its `snapshot` and `record-origin` steps on the untouched copy before any change, so later updates can merge. Never write its `.ah-upstream.json` file by hand: a wrong one breaks later merges. Without `import-updates`, note the plugin, skill, version and where it came from in `run.md`.
- Save a backup of the fresh copy before its first edit. Change the description only if triggering is actually the problem.
