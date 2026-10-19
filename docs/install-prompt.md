# Attendee installation prompt

The current candidate adds Humanizer alongside the merged Skill Studio package. After that PR is merged, this prompt installs both from the default branch. The repository remains private; current testers need GitHub read access. Earlier Skill Studio-only public prompt tests are historical evidence in [public-prompt-test.json](public-prompt-test.json); two-plugin validation is recorded separately in [humanizer-verification.json](humanizer-verification.json).

Copy this prompt into the local client you want to use:

```text
Install Skill Studio 0.10.0-dcbkk.1 and Humanizer 1.2.2-dcbkk.1 from the GitHub marketplace Authority-Hacker/dcbkk-plugins. Install only skill-studio@dcbkk-plugins and humanizer@dcbkk-plugins.

First identify whether this is Codex or Claude Code and use that client's supported installation method. Use the same local environment as this chat.

Codex terminal:
codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git
codex plugin add skill-studio@dcbkk-plugins
codex plugin add humanizer@dcbkk-plugins

Claude Code terminal:
claude plugin marketplace add Authority-Hacker/dcbkk-plugins
claude plugin install skill-studio@dcbkk-plugins
claude plugin install humanizer@dcbkk-plugins

Claude Code chat equivalents use /plugin marketplace add and /plugin install with the same source and plugin ID. Don't run Claude commands in Codex or invent a universal chat command.

If you can't run the installation here, give me only the steps for my client. If another Skill Studio or Humanizer copy is enabled, ask which copy to keep; preserve my other plugins and personal skills. While the repo is private, use my authorized GitHub access. Don't ask for AH membership, paste credentials into chat, or bypass repository permissions.

Verify Skill Studio 0.10.0-dcbkk.1 and Humanizer 1.2.2-dcbkk.1 are installed and enabled. Tell me if I need to restart/reload or start a new chat. After that, confirm only skill-studio:skill-studio and humanizer:humanizer are listed for this marketplace in the skill/slash menu. The router must still be able to use create-skill, improve-skill and tidy-skill internally. Don't claim a terminal install proves the desktop app loaded them.

Then ask whether I want to save a repeated workflow with Skill Studio or edit an existing draft with Humanizer. Use the relevant main skill on my real input. If it does not trigger naturally, select skill-studio:skill-studio or humanizer:humanizer explicitly. Say what was verified and what still needs checking.
```
