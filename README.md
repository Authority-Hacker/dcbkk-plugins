# DCBKK plugins

Skill Studio **0.10.0** for Codex and Claude Code. One plugin, four skills: learn how you work, create a skill, improve one, or tidy one that has grown messy.

This marketplace is private until Gael explicitly approves making it public. Private testers need GitHub read access and working Git authentication. The plugin itself needs no Authority Hacker membership, API key, MCP server, or paid add-on. Use your own supported client and model account.

## Install

These GitHub commands apply once the marketplace PR is merged into the repository's default branch. Before merging, test its branch explicitly; see [release notes](docs/release.md). The private repository is [Authority-Hacker/dcbkk-plugins](https://github.com/Authority-Hacker/dcbkk-plugins). Until the PR is merged, its default branch is an empty bootstrap base; use the branch instructions in the release notes for private testing.

**Codex terminal**

```sh
codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git
codex plugin add skill-studio@dcbkk-plugins
codex plugin list --marketplace dcbkk-plugins --json
```

Quit and reopen Codex, then start a new chat in the same local environment. In the desktop app, confirm **DCBKK Plugins → Skill Studio** is installed and enabled. A terminal install alone does not prove the desktop app loaded it: the CLI and app must use the same local Codex home. If the CLI lacks `plugin`, use a current supported client; do not substitute another marketplace.

**Claude Code terminal**

```sh
claude plugin marketplace add Authority-Hacker/dcbkk-plugins
claude plugin install skill-studio@dcbkk-plugins
claude plugin list --json
```

In a Claude Code chat, the equivalents are `/plugin marketplace add Authority-Hacker/dcbkk-plugins` and `/plugin install skill-studio@dcbkk-plugins`. Start a new session after installing, or use `/reload-plugins`, then confirm the plugin is enabled through `/plugin`.

**Check it works:** in a new chat, say “Use Skill Studio. Help with this task and remember how I like it,” followed by a real task. It should use the Skill Studio entry point and the relevant route. Confirm all four skills are available: `skill-studio`, `create-skill`, `improve-skill`, and `tidy-skill`. If routing misses it, choose the namespaced `skill-studio:skill-studio` entry from your client's skill picker.

If another marketplace already supplies Skill Studio, choose which copy to keep enabled before using it. Don't remove other plugins or personal skills to fix an install. While this repo is private, a GitHub permission error requires an authorized GitHub account; it is not an AH activation step.

The [attendee prompt](docs/install-prompt.md) is ready to copy after the default branch is populated and verified. Public access remains a separate release decision.

## Source and checks

The complete plugin folder is byte-identical to `plugins/skill-studio` at student staging commit `1aad3456c7cbb3320d3b1fb4160c9ebe974a3a6e`. The live staging gateway delivered the same skills and supporting content as version 0.10.0 at bundle commit `8b5918effe262901ff7fc310a9d3c046a3521523` on 18 October 2026. Its manifests add staging names; this repo preserves the original upstream plugin identity. Only the marketplace is named `dcbkk-plugins`.

The direct staging GitHub bundle branch was stale at `88cc5a8794f45190c90e6e9951ef27a91c2fe042` (0.6.0); it was not used. The installed 0.10.0 staging copy's skills and supporting files also matched. Exact per-file hashes and the aggregate digest are in [source-lock.json](docs/source-lock.json).

```sh
python3 scripts/verify.py
claude plugin validate --strict .
```

The plugin has no required third-party runtime dependency. Its optional checker uses Python 3's standard library, with manual checking when Python is unavailable. AH Utility's optional updater is used only if already installed. Skill Studio keeps its work notes under `~/.claude/skill-studio-work/`, including when used in Codex; that behavior is preserved from upstream.

[Verification and release handoff](docs/release.md) records actual evidence and remaining checks. Catalog formats follow [OpenAI's packaging documentation](https://developers.openai.com/plugins/build/plugins) and [Claude Code's marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).
