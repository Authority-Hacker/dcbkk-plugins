# Attendee installation prompt

PR #1 is merged. This prompt passed anonymous GitHub installation tests with both clients on 18 October 2026 during an approved brief public window. The repo is private again. Private testers currently need GitHub read access; public attendees will not need that after the final public release. See [test evidence](public-prompt-test.json) for method and limits.

Copy this prompt into the local client you want to use:

```text
Install Skill Studio 0.10.0 from the GitHub marketplace Authority-Hacker/dcbkk-plugins. Install only skill-studio@dcbkk-plugins.

First identify whether this is Codex or Claude Code and use that client's supported installation method. Use the same local environment as this chat.

Codex terminal:
codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git
codex plugin add skill-studio@dcbkk-plugins

Claude Code terminal:
claude plugin marketplace add Authority-Hacker/dcbkk-plugins
claude plugin install skill-studio@dcbkk-plugins

Claude Code chat equivalents use /plugin marketplace add and /plugin install with the same source and plugin ID. Don't run Claude commands in Codex or invent a universal chat command.

If you can't run the installation here, give me only the steps for my client. If another Skill Studio copy is enabled, ask which copy to keep; preserve my other plugins and personal skills. While the repo is private, use my authorized GitHub access. Don't ask for AH membership, paste credentials into chat, or bypass repository permissions.

Verify version 0.10.0 is installed and enabled. Tell me if I need to restart/reload or start a new chat. After that, confirm these four skills are visible: skill-studio, create-skill, improve-skill, tidy-skill. Don't claim a terminal install proves the desktop app loaded them.

Then ask me for a small real task and use Skill Studio on it. If it doesn't trigger naturally, select the skill-studio:skill-studio entry explicitly. Say what was verified and what still needs checking.
```
