# Private verification and release handoff

Status: locally prepared; GitHub creation and first push blocked by automatic approval review. No remote repository, PR, CI, or privacy readback yet. No production/staging service changed. No public visibility change, deployment, event announcement, or automatic release scheduled.

## Evidence from 18 October 2026

- Pinned version: **0.10.0**. See `source-lock.json` for the exact student source, live gateway bundle, and all 19 file hashes. Event package content is unchanged from that student commit. Gateway and installed staging versions differ only in their two identity manifests.
- Claude Code **2.1.302**: strict marketplace validation passes. Its informational advice suggests an install line inside the bundled README; that README stays unchanged to preserve the pinned artifact. Installation in a disposable `CLAUDE_CONFIG_DIR` succeeds, lists version 0.10.0 enabled, and all 19 installed file hashes match.
- Codex CLI **0.163.0**: local marketplace add and plugin install in a disposable `CODEX_HOME` succeed. `plugin list` reports version 0.10.0 installed and enabled. All 19 installed file hashes match. A fresh app-server `skills/list` scan discovers all four enabled event-plugin skills with `pluginId: skill-studio@dcbkk-plugins` and paths inside the disposable installed package. The profile still sees the operator's personal skills outside `CODEX_HOME`; the event entries were filtered by plugin ID for this check. This is isolated plugin configuration, not a completely empty machine.
- Claude runtime invocation: a fresh session loaded `skill-studio:skill-studio` through the Skill tool, read `references/learn-from-work.md`, rewrote the note to “Doors open at 9am. Please bring your laptop.”, and stopped before saving as requested. The first harness denied the reference read because the plugin directory was outside its read scope; adding that exact package directory repaired the harness, with no permission denials. The final output initially labelled the note “16 words” then correctly counted 8; this small output-quality error is recorded, not hidden. This checks one entry-point route, not the full create/improve/tidy workflows.
- Disposable Codex model invocation is not verified: automatic approval review rejected linking the existing credential file into the profile. Credentials were not copied or linked. The profile remains unauthenticated. Desktop UI acceptance, remote GitHub installation, fresh account testing, and unauthenticated public installation are not verified.

## Finish the private repository

After approval for the blocked GitHub actions: create `Authority-Hacker/dcbkk-plugins` as PRIVATE, push a minimal bootstrap base, then put the complete marketplace on `codex/add-skill-studio` and open a PR. Read back `isPrivate: true`. Do not merge automatically. Before calling the PR ready, check its changed files, CI if present, reviews and mergeability.

Test branch installs before merging. For Codex use `codex plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git --ref codex/add-skill-studio`. For Claude Code use `claude plugin marketplace add https://github.com/Authority-Hacker/dcbkk-plugins.git#codex/add-skill-studio`. Install `skill-studio@dcbkk-plugins`, check all 19 installed hashes and the four loaded skills, and invoke the entry point in a fresh session. Test these branch commands before relying on them; only local-path installs have been verified so far.

Once merged by Gael, rerun from the default branch, update this status, and use the attendee prompt without a branch override. No source tokens or AH member gateway URLs belong in the event repository.

## Public release is a later decision

1. Get Gael's explicit approval to change GitHub visibility. Confirm the desired redistribution/license terms; none are invented here.
2. Check the exact default-branch package hash, catalogs, README and attendee prompt. Ensure only Skill Studio is distributed and no credentials, private gateway URLs, local machine paths, or unrelated material are included.
3. Make the approved visibility change, then read back `isPrivate: false`.
4. From unauthenticated, clean Git/client environments, test GitHub clone and both client installations, installed hashes, four visible skills, and a meaningful Skill Studio entry point. Check Codex desktop separately from its CLI. No AH membership should be required.
5. If any check fails, hold attendee distribution and diagnose. This checklist does not authorize announcement, website publication, spending, or changes to other marketplaces.

The eventual event resource route `authorityhacker.com/aibuildlab/` is outside this repo and this task. No website is implemented or deployed here.
