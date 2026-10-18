# Private verification and release handoff

Status: [PR #1](https://github.com/Authority-Hacker/dcbkk-plugins/pull/1) merged on 18 October 2026 at `4c06d83520b282bb9eaf3dc7c5b7a3c63a1fd5c0`. The default branch contains the complete marketplace. Gael approved a short public window for anonymous prompt testing; both clients passed. The repository is PRIVATE again (`isPrivate: true` independently read back), with no forks at final readback. No CI is configured. No production/staging service, website, or announcement was changed. Final public release remains separate.

## Evidence from 18 October 2026

- Pinned version: **0.10.0**. See `source-lock.json` for the exact student source, live gateway bundle, and all 19 file hashes. Event package content is unchanged from that student commit. Gateway and installed staging versions differ only in their two identity manifests.
- Claude Code **2.1.302**: strict marketplace validation passes. Its informational advice suggests an install line inside the bundled README; that README stays unchanged to preserve the pinned artifact. Installation in a disposable `CLAUDE_CONFIG_DIR` succeeds, lists version 0.10.0 enabled, and all 19 installed file hashes match.
- Codex CLI **0.163.0**: local marketplace add and plugin install in a disposable `CODEX_HOME` succeed. `plugin list` reports version 0.10.0 installed and enabled. All 19 installed file hashes match. A fresh app-server `skills/list` scan discovers all four enabled event-plugin skills with `pluginId: skill-studio@dcbkk-plugins` and paths inside the disposable installed package. The profile still sees the operator's personal skills outside `CODEX_HOME`; the event entries were filtered by plugin ID for this check. This is isolated plugin configuration, not a completely empty machine.
- Claude runtime invocation: a fresh session loaded `skill-studio:skill-studio` through the Skill tool, read `references/learn-from-work.md`, rewrote the note to “Doors open at 9am. Please bring your laptop.”, and stopped before saving as requested. The first harness denied the reference read because the plugin directory was outside its read scope; adding that exact package directory repaired the harness, with no permission denials. The final output initially labelled the note “16 words” then correctly counted 8; this small output-quality error is recorded, not hidden. This checks one entry-point route, not the full create/improve/tidy workflows.
- Disposable Codex model invocation is not verified: automatic approval review rejected linking the existing credential file into the profile. Credentials were not copied or linked. The profile remains unauthenticated. Desktop UI acceptance and fresh model-account testing are not verified. Anonymous GitHub installation is now verified as described below.

## Default branch and public prompt verification

Repository: [Authority-Hacker/dcbkk-plugins](https://github.com/Authority-Hacker/dcbkk-plugins). Both private authenticated branch installs and default-branch anonymous installs passed. [PR #1](https://github.com/Authority-Hacker/dcbkk-plugins/pull/1) is merged; regular attendee commands now resolve the complete marketplace. It remains private except during approved tests.

The exact attendee prompt was tested in separate Codex and Claude Code model sessions, with one harness adaptation: installation used disposable client profiles to preserve the operator's settings. Both models ran the correct app-specific commands, installed only 0.10.0, checked enabled state and all four packaged skills, then requested a real task. Both correctly stated that loading requires a fresh session and did not equate CLI installation with desktop acceptance.

Git authentication was disabled in these tests. Anonymous access failed while private, then succeeded while public. The first cycle ended safely after 5.7 seconds because anonymous Git access had not yet caught up with GitHub's public readback. A bounded readiness retry repaired the test: anonymous Git became ready on the third check, and both prompt tests completed. The successful visibility-change/test/restore cycle took 46.7 seconds. Both cycles restored PRIVATE through a `finally` block and readback; the operator's plugin settings remained unchanged. Details are in [public-prompt-test.json](public-prompt-test.json).

All 19 public-installed file hashes match the source lock. A fresh Codex app-server scan discovers all four enabled event-plugin skills from that cache. A fresh Claude session also invoked `skill-studio:skill-studio` from the public-installed package, read `learn-from-work.md`, and produced the correct eight-word draft with no permission denials or file writes. Model-account authentication was normal; only Git repository access was anonymous. These tests do not prove a completely fresh machine, fresh model account, or Codex desktop UI. No credentials were copied into test profiles. A later private readback reported zero forks, which cannot prove that no one cloned the briefly public repository.

## Public release is a later decision

1. Get Gael's explicit approval to change GitHub visibility. Confirm the desired redistribution/license terms; none are invented here.
2. Check the exact default-branch package hash, catalogs, README and attendee prompt. Ensure only Skill Studio is distributed and no credentials, private gateway URLs, local machine paths, or unrelated material are included.
3. Make the approved visibility change, then read back `isPrivate: false`.
4. From unauthenticated, clean Git/client environments, test GitHub clone and both client installations, installed hashes, four visible skills, and a meaningful Skill Studio entry point. Check Codex desktop separately from its CLI. No AH membership should be required.
5. If any check fails, hold attendee distribution and diagnose. This checklist does not authorize announcement, website publication, spending, or changes to other marketplaces.

The eventual event resource route `authorityhacker.com/aibuildlab/` is outside this repo and this task. No website is implemented or deployed here.
