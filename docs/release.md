# Private verification and release handoff

Status: PRIVATE GitHub repository created with direct approval on 18 October 2026; `isPrivate: true` confirmed via GitHub readback. Marketplace is on `codex/skill-studio-marketplace`; the default `main` is an empty bootstrap base until Gael merges the PR. No CI is configured; local package checks and actual client installs provide the validation. No production/staging service changed. No public visibility change, deployment, event announcement, or automatic release scheduled.

## Evidence from 18 October 2026

- Pinned version: **0.10.0**. See `source-lock.json` for the exact student source, live gateway bundle, and all 19 file hashes. Event package content is unchanged from that student commit. Gateway and installed staging versions differ only in their two identity manifests.
- Claude Code **2.1.302**: strict marketplace validation passes. Its informational advice suggests an install line inside the bundled README; that README stays unchanged to preserve the pinned artifact. Installation in a disposable `CLAUDE_CONFIG_DIR` succeeds, lists version 0.10.0 enabled, and all 19 installed file hashes match.
- Codex CLI **0.163.0**: local marketplace add and plugin install in a disposable `CODEX_HOME` succeed. `plugin list` reports version 0.10.0 installed and enabled. All 19 installed file hashes match. A fresh app-server `skills/list` scan discovers all four enabled event-plugin skills with `pluginId: skill-studio@dcbkk-plugins` and paths inside the disposable installed package. The profile still sees the operator's personal skills outside `CODEX_HOME`; the event entries were filtered by plugin ID for this check. This is isolated plugin configuration, not a completely empty machine.
- Claude runtime invocation: a fresh session loaded `skill-studio:skill-studio` through the Skill tool, read `references/learn-from-work.md`, rewrote the note to “Doors open at 9am. Please bring your laptop.”, and stopped before saving as requested. The first harness denied the reference read because the plugin directory was outside its read scope; adding that exact package directory repaired the harness, with no permission denials. The final output initially labelled the note “16 words” then correctly counted 8; this small output-quality error is recorded, not hidden. This checks one entry-point route, not the full create/improve/tidy workflows.
- Disposable Codex model invocation is not verified: automatic approval review rejected linking the existing credential file into the profile. Credentials were not copied or linked. The profile remains unauthenticated. Desktop UI acceptance, fresh account testing, and unauthenticated public installation are not verified.

## Private GitHub verification

Repository: [Authority-Hacker/dcbkk-plugins](https://github.com/Authority-Hacker/dcbkk-plugins). Direct approval resolved the earlier automatic review block on creation/first push. An empty base was created separately from the marketplace change; no plugin content was committed directly to `main`. The marketplace PR remains unmerged.

Test branch installs before merging. For Codex use `codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git --ref codex/skill-studio-marketplace`. For Claude Code use `claude plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git#codex/skill-studio-marketplace`. Install `skill-studio@dcbkk-plugins`, check all 19 installed hashes and the four loaded skills, and invoke the entry point in a fresh session. Both branch commands were tested with authenticated GitHub access in new disposable profiles. Both clients report 0.10.0 enabled, with all 19 installed file hashes matching. A fresh Codex app-server scan finds all four enabled event-plugin skills from this remote install. Claude also invoked `skill-studio:skill-studio` from its GitHub-installed cache, read the learn-from-work reference, and completed the draft-only note task with an accurate word count and no permission denials or file writes. These tests use the operator’s authorized GitHub account; they do not prove public/unauthenticated access.

Once merged by Gael, rerun from the default branch, update this status, and use the attendee prompt without a branch override. No source tokens or AH member gateway URLs belong in the event repository.

## Public release is a later decision

1. Get Gael's explicit approval to change GitHub visibility. Confirm the desired redistribution/license terms; none are invented here.
2. Check the exact default-branch package hash, catalogs, README and attendee prompt. Ensure only Skill Studio is distributed and no credentials, private gateway URLs, local machine paths, or unrelated material are included.
3. Make the approved visibility change, then read back `isPrivate: false`.
4. From unauthenticated, clean Git/client environments, test GitHub clone and both client installations, installed hashes, four visible skills, and a meaningful Skill Studio entry point. Check Codex desktop separately from its CLI. No AH membership should be required.
5. If any check fails, hold attendee distribution and diagnose. This checklist does not authorize announcement, website publication, spending, or changes to other marketplaces.

The eventual event resource route `authorityhacker.com/aibuildlab/` is outside this repo and this task. No website is implemented or deployed here.
