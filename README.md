# DCBKK plugins

Skill Studio **0.10.0**, event package **0.10.0-dcbkk.1**, for Codex and Claude Code. Its single menu entry covers learning how you work, creating a skill, improving one, or tidying one that has grown messy.

**Humanizer 1.2.2-dcbkk.1** adds natural-sounding edits and pattern-only reviews, based on published Content Humanizer 1.2.2. Its marketplace and skill name are both `humanizer`. The marketplace contains only these two plugins and exposes one menu entry for each.

This marketplace is private until Gael explicitly approves making it public. Private testers need GitHub read access and working Git authentication. The plugin itself needs no Authority Hacker membership, API key, MCP server, or paid add-on. Use your own supported client and model account.

## Install

[PR #1](https://github.com/Authority-Hacker/dcbkk-plugins/pull/1) is merged. These commands install from the default branch. The repository is private again after the approved brief anonymous installation test; until the final public release, testers need authorized GitHub read access.

**Codex terminal**

```sh
codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git
codex plugin add skill-studio@dcbkk-plugins
codex plugin add humanizer@dcbkk-plugins
codex plugin list --marketplace dcbkk-plugins --json
```

Quit and reopen Codex, then start a new chat in the same local environment. In the desktop app, confirm **DCBKK Plugins → Skill Studio** is installed and enabled. A terminal install alone does not prove the desktop app loaded it: the CLI and app must use the same local Codex home. If the CLI lacks `plugin`, use a current supported client; do not substitute another marketplace.

**Claude Code terminal**

```sh
claude plugin marketplace add Authority-Hacker/dcbkk-plugins
claude plugin install skill-studio@dcbkk-plugins
claude plugin install humanizer@dcbkk-plugins
claude plugin list --json
```

In a Claude Code chat, the equivalents are `/plugin marketplace add Authority-Hacker/dcbkk-plugins` and `/plugin install skill-studio@dcbkk-plugins`. Start a new session after installing, or use `/reload-plugins`, then confirm both plugins are enabled through `/plugin`. Install Humanizer in chat with `/plugin install humanizer@dcbkk-plugins`.

**Check it works:** in a new chat, say “Use Skill Studio. Help with this task and remember how I like it,” followed by a real task. It should use the Skill Studio entry point and the relevant route. For Skill Studio, only the `skill-studio:skill-studio` router should appear in the skill menu. Humanizer adds exactly one other entry, `humanizer:humanizer`. It chooses create, improve, or tidy internally. If routing misses it, choose the namespaced `skill-studio:skill-studio` entry from your client's skill picker.

If another marketplace already supplies Skill Studio, choose which copy to keep enabled before using it. Don't remove other plugins or personal skills to fix an install. While this repo is private, a GitHub permission error requires an authorized GitHub account; it is not an AH activation step.

The original 0.10.0 [attendee prompt](docs/install-prompt.md) passed separate Codex and Claude Code installation tests during a brief approved public window. The menu patch is verified separately; its installation commands are unchanged. Public access is now closed again; the final public release remains a separate decision.

## Update an existing test install

After this PR is merged, refresh the marketplace and plugin in the same profile you installed into:

```sh
codex plugin marketplace upgrade dcbkk-plugins
codex plugin add skill-studio@dcbkk-plugins
```

For Claude Code:

```sh
claude plugin marketplace update dcbkk-plugins
claude plugin update skill-studio@dcbkk-plugins
```

Reload or start a new session, then check the installed version is `0.10.0-dcbkk.1` and only the router is listed.

## Humanizer source and checks

Humanizer comes from the canonical student `main` commit `2a72da5839916f2a0dcde5e7bd450af2f6d989ba`, byte-identical to the published production bundle at `9162b534ab928fa00ab6c60b2a94dcae084b743a` before the event alias. Its main skill is already the only skill, so no hidden specialists or discovery changes are needed. The event alias changes identity, headings and literal skill paths; its editing rules, references, scanner logic, changelog and license are preserved. [Source lock](docs/humanizer-source-lock.json) retains both upstream and event hashes; the verifier reverses only the documented alias changes and proves every original file hash.

It has no AH login, MCP, provider or paid API dependency. Its read-only scanner uses Python 3 standard-library modules; normal edits do not require it. The bundled MIT license and copyright attribution are retained. [Humanizer validation](docs/humanizer-verification.json) records install, menu and runtime checks.

## Skill Studio source and checks

The workflow bodies and all supporting files are unchanged from `plugins/skill-studio` at student staging commit `1aad3456c7cbb3320d3b1fb4160c9ebe974a3a6e`. The live staging gateway delivered the same skills and supporting content as version 0.10.0 at bundle commit `8b5918effe262901ff7fc310a9d3c046a3521523` on 18 October 2026. Its manifests add staging names; this repo preserves the original upstream plugin identity. Only the marketplace is named `dcbkk-plugins`. This event patch adds `user-invocable: false` to the three specialists for Claude, limits Codex discovery to `./skills/skill-studio`, and gives the package its own version so existing 0.10.0 caches are not reused. The router follows its unchanged links to specialists in Codex. [Menu verification](docs/router-menu.json) records the live client checks; original upstream and event hashes are preserved separately in the source lock.

The direct staging GitHub bundle branch was stale at `88cc5a8794f45190c90e6e9951ef27a91c2fe042` (0.6.0); it was not used. The installed 0.10.0 staging copy's skills and supporting files also matched. Exact per-file hashes and the aggregate digest are in [source-lock.json](docs/source-lock.json).

```sh
python3 scripts/verify.py
claude plugin validate --strict .
```

The plugin has no required third-party runtime dependency. Its optional checker uses Python 3's standard library, with manual checking when Python is unavailable. AH Utility's optional updater is used only if already installed. Skill Studio keeps its work notes under `~/.claude/skill-studio-work/`, including when used in Codex; that behavior is preserved from upstream.

[Verification and release handoff](docs/release.md) records actual evidence and remaining checks. Catalog formats follow [OpenAI's packaging documentation](https://developers.openai.com/plugins/build/plugins) and [Claude Code's marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).
