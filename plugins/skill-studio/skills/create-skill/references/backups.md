# Backups and putting it back

Before changing a skill that already exists, save a copy. That is what makes "if you don't like it, I can put it back" true.

## Where they live

`~/.claude/skill-studio-work/<skill-name>/backups/` holds one folder per save, named by date and time (`YYYYMMDD-HHMMSS`), and an `index.md` beside them. This is outside every folder the assistant loads skills from, so a backup never shows up as a second skill. For a project skill that shares its name with a personal one, use `<skill-name>--<project>`.

## Saving

1. Copy the whole skill folder into a new backup folder. Never write into an existing one; if the name is taken, add `-2`.
2. Re-read the copy against the live skill: same files, same contents.
3. Add one line to `index.md`: the date, what is about to change in the person's words, and why if they said ("17 Oct 14:02, before 'always put the date first': clients scan for it"). Don't ask for a reason just for the label. The index sits beside the copies, never inside one, so restoring a copy never brings the notes with it.
4. Say "I kept a backup first."

If the copy fails, don't edit.

## Putting it back

1. List the saves from `index.md`, newest first, in the person's words. If they already said which one, don't ask again.
2. Save the current version first, as above ("before putting back the 3 Oct version"), so changing their mind later is safe.
3. Replace the live folder with the chosen copy as a whole. Never copy over the top: files added since would survive.
4. Re-read the result against the chosen copy and say which version is back.

Restoring is the whole job. Don't go on to improve the skill in the same step.

## Reading an old version

To compare old and new, as a tidy does, read the copy where it is. Don't restore it.

## Older saves

Earlier versions of Skill Studio kept saves in `~/.claude/skill-history/`, a git repository. Each skill there is a folder plus a notes file beside it, named `<skill-name>` and `<skill-name>.md`, or `<skill-name>--<project>` for a project skill that shared a personal skill's name. If that history exists, list its saves too, using both names: `git -C ~/.claude/skill-history log --oneline -- <name> <name>.md`. To restore one:

1. Write that commit to a new empty folder: `git -C ~/.claude/skill-history archive --format=tar -o <new folder>/old.tar <commit> <name> <name>.md`, then `tar -xf old.tar` inside it.
2. The extracted notes file lists the saved folder's contents. Recreate any empty folders it records, which git leaves out.
3. Use the extracted `<name>` folder in step 3 above.

If git isn't installed, say those older saves need it. Never delete that folder.

Never commit anything into the person's own project. If the skill lives in a project that uses git, say what changed and leave the commit to them.
