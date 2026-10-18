# Changelog — Skill Studio

## 0.10.0 - 2026-10-17

### What changed

- Before writing a skill, Skill Studio now clarifies with you what a great result looks like. It looks things up first, then asks one question at a time, each with its own best guess. When there's no clear standard yet, such as no example you're happy with or work that has to perform (reels, posts, emails that need replies), it covers what a win is, who it's for, and one you loved, yours or someone else's. With clear rules and an example you like, it usually asks nothing.
- It studies great examples before writing: your best ones first, then the ones you admire. If you want, it can research top performers too, after asking, since that can cost money.
- It shows you its plan for getting from your material to a great result before it drafts, then shows you a real trial and asks what you'd change before it asks where to install.

### Why it matters

- Skills for content that has to perform now start from an agreed standard and real examples. Your call notes and transcripts supply the material; your goals and the examples you like set what good looks like.

### What you need to do

- Nothing. Quick skills with an example you're happy with still go straight through.

### If you customized this plugin

- `create-skill/references/clarify.md` is new. The "no work to learn from" questions in `interview-guide.md` moved into it.

## 0.9.0 - 2026-10-17

### What changed

- Skill Studio may ask a quick "why" about your corrections ("Is that because your clients read on their phones?"). Your skill then stores each rule with its reason, so it handles the next task too, not just a replay of this one.
- Skills are checked against every one of your rules when they're tried. A skill learned from one example is tried again with the details swapped, so client names and this week's numbers don't get baked in.
- Skills can use more than plain instructions when the job needs it: a check-and-revise loop, a fact check before delivery, helper agents for big research or a second opinion, or a page for picking between many options. Skill Studio adds one only when it fixes a real problem, and tells you what it costs.
- If a skill will spend money or send things for you, you approve that once while it's built. Skill Studio no longer runs a separate review or asks you to approve connectors and commands.
- Tidy now does real cleanup. After lots of quick changes, it rebuilds a skill into one clean, coherent version, merges rules that pile up, asks you about rules that clash, and accounts for every rule so nothing is lost. Skills offer a tidy after about ten quick changes.
- Backups are plain copies with a label for each change, so "put it back" shows choices like "before 'always put the date first'". Git is no longer needed.
- New skills use only the two settings both Claude Code and Codex understand, and the file check flags anything else.

### Why it matters

- Skills get the next task right more often, stay lean as you keep correcting them, and building one no longer involves a technical review process.

### What you need to do

- Nothing. Your existing skills keep working, and saves made by earlier versions in `~/.claude/skill-history/` can still be restored.

### If you customized this plugin

- The review files (`review-convergence.md`, `review-checklist.md`, `safety-rails.md`), `paths.md`, `first-use-and-comparison.md` and `skill-history.md` are gone. Their remaining rules now live in `create-skill/SKILL.md`, `run-policy.md` and the new `backups.md`. `mechanics.md` is new, and `tidy-skill` and `tidy-rules.md` were rewritten.

## 0.8.0 - 2026-10-13

### What changed

- You can start with a task instead of a skill. Ask for help with real work and correct the result, then say "save that". Skill Studio keeps your lasting preferences and leaves out one-off details.
- Small skills are quick: written and tried on your example in one go, then installed where you choose. The thorough independent check is kept for skills that run code, send or post things, handle accounts, or change an Authority Hacker plugin skill.
- New skills include a self-update section (you can ask for one without it). Say "remember", "always" or "never" while using one, and it saves the rule after keeping a backup. Changes to scripts or anything that sends or spends still go through Skill Studio.
- Changing a preference in an existing skill is now a quick, backed-up edit instead of a full repair.
- Replies use plain language instead of technical terms.

### Why it matters

- Simple skills no longer take a long, technical process, and skills get better as you use them instead of needing to be perfect up front.

### What you need to do

- Nothing. Skills you made with earlier versions keep working. To give an older skill the self-update ability, ask Skill Studio to add it.

### If you customized this plugin

- Your copy keeps working. The new behavior is in the `skill-studio` front door, the new `paths.md` and `learn-from-work.md` references, and the self-update section in `skill-template.md`.

## 0.7.0 - 2026-09-30

- Adds a lean `skill-studio` intent router that invokes one focused specialist, carries the existing request/state forward and preserves all three direct entry points.

- Complete supplied briefs proceed without mandatory interview, plan confirmation or repeated output sign-off. Missing material judgment still gets a focused question.
- Create, improve and tidy share authorization, record and proof rules. Existing informed approvals carry forward for the same action scope; new risky behavior still needs independent review and explicit authority before execution or activation.
- Every lane preserves real-input coverage, complete-artifact review, bounded defect repair, exact replacement/recovery and AH fork provenance. Tidy audits inline by default and keeps isolated old/new semantic proof.
- Documents Claude Code and Codex targets without migrating existing skills. A create request produces a candidate unless installation into an exact scope is approved.
- Fixes inherited checker metadata secret leakage and symlink reads; skipped items are explicit manual-coverage flags. Recovery verifies the durable Git snapshot and reconstructs recorded empty directories before claiming exact restore.
- No new dependency, provider, account or global installation. Git history and optional Python checker remain. Live updater/installed-host routing and Windows behavior have not been tested by this modernization.

## 0.6.0 - 2026-08-20

### What changed

- When Skill Studio copies an AH plugin skill for customization, it now uses `import-updates` to verify the copy byte-for-byte and records the exact source commit in `.ah-upstream.json` before editing begins.
- It no longer uses the updater's finalization command as a shortcut for recording a new fork.

### Why it matters

- The source record moves with your customized skill, so moving or renaming its folder does not prevent a later AH update from finding the right original version and preserving your work.

### What you need to do

- Nothing. Keep AH Utility installed when forking an AH skill if you want future updates to merge automatically.

### If you customized this plugin

- Existing forks keep working with their current history. Forks created after this release receive the portable source record automatically when AH Utility is available.

## 0.5.0 — 2026-07-29

This release makes review converge across create, improve, and tidy without
weakening real safety or output-integrity gates.

### Added
- **A shared convergence contract.** Every lane uses the same release packet,
  finding register, severity definitions, available-cost record, and two-pass
  ceiling.
- **Core-promise coverage.** Real-input checks now prove the defining behavior
  they claim to cover instead of letting one pleasant example stand in for
  untested paths.
- **A load-bearing component check.** After the first failed review, optional
  scripts, hooks, integrations, and templates are reconsidered before another
  repair pass.

### Changed
- The first review remains broad. The second verifies prior blockers, changed
  surfaces, and frozen regressions; it is not a fresh defect hunt.
- Findings are separated into install blockers, optional-component blockers,
  and hardening backlog. Reviewers cannot inflate severity without a
  reproduction or direct evidence against the confirmed contract.
- Independent reviewers receive the prior findings, dispositions, accepted
  tradeoffs, exact changed scope, and round cost. Fresh judgment no longer means
  blank context.
- Components with their own contracts, dependencies, side effects, or
  substantial test burden route to a separate software workflow. This is based
  on failure surface, not line count or a blanket rule against scripts.
- After a failed second pass, every lane stops with explicit remove, narrow,
  restore/park, or bounded-exception choices. No third pass starts
  automatically.

## 0.4.0 — 2026-07-28

This release makes the three workflows harder for an agent to half-follow, skip, or falsely declare finished.

### Added
- **A non-shipping run ledger.** Create keeps its plan, evidence, checks, approvals, and outcome with the draft in `~/.claude/skill-studio-work/<skill-name>/`. Improve and tidy append the same facts to `~/.claude/skill-history/<skill-name>.md`. Secrets and full transcripts never belong there.
- **Fresh-chat restore.** Improve can list saved versions, preserve the current state, restore the selected commit, verify exact bytes, record the result, and stop.
- **Risk-gated executable surfaces.** New or materially changed shell, network, environment, hooks, external writes, or destructive behavior must be named by a fresh reviewer and approved in the same turn. Existing unchanged behavior is inventoried without needless reapproval. Embedded secrets still block absolutely.
- **Junk-aware tidy checks.** Low-risk cache artifacts can be removed automatically; repositories, environment files, dependencies, builds, virtual environments, broad directories, and uncertain contents require a checkpoint.

### Changed
- Each workflow stage now has a concrete input, output, owner, exit gate, and failure route.
- Create now stops on an empty judgment core, broken trigger, rejected permission surface, or embedded secret; it also says when there is no real moat and no skill should be built.
- Create distinguishes optional past-work exemplars from the real input required for test-driving, treats incomplete lint as manual-review work, accepts open corrections to its plan, and replaces an installed folder exactly instead of overlaying it.
- Improve inventories the whole skill before choosing patch, fork, or rebuild; proves diagnosis against exact evidence; caps repair at two failed cycles; and offers restore or rebuild instead of looping.
- Tidy persists its audit queue before editing, checks helper availability before semantic work, uses exhaustive proof tiers, and reports every finding as cut, kept, moved, rewritten, skipped, failed, or unproved.
- Plugin forks keep the original skill name. The README no longer suggests a contradictory renamed-copy fallback.

### Verified
- Added regression coverage for restore routing, fork ordering, exact replacement, lint fallback, permission checkpoints, junk classification, and proof routing.
- Re-ran the three trigger sets, focused hard cases, formal test-drives, an uncooperative student simulation, plugin validation, safety and permission scans, and the repository doctor before staging.

## 0.3.0 — 2026-07-27

The release that makes every change to an existing skill undoable, and stops the plugin promising things it couldn't deliver.

### Added
- **A saved history for every skill.** `~/.claude/skill-history/` keeps the version that worked before each change, so "put it back the way it was" returns the exact original. Used by all three skills; replaces tidy-skill's backup folder, which restored its own notes into the live skill.
- **A stop when git is missing.** Skill Studio now checks for git before the first change and walks you through installing it on macOS, Windows, or Linux. No recovery point, no edits.
- **Fork provenance.** Copying a plugin's skill into your own folder now records which release it came from, so AH's `import-updates` can merge a later AH update into your customized copy properly instead of guessing.
- **A README.**

### Changed
- **Forking a plugin skill now silences the original.** It used to rename your copy and leave the plugin's version live, competing for the same request — so your fix could look like it randomly didn't apply. Silencing is now a required step with a stated method, and you're told in one sentence which version answers.
- **"It never fires" is now a complaint improve-skill accepts.** It used to demand the output that went wrong, which a skill that never runs cannot produce. It now takes what you typed as the example, and closes honestly: whether a skill fires is only visible in a new chat, so it asks you to try there rather than claiming an in-chat test proved anything.
- **The checker now sees the version that ships.** All three skills re-run it over the final version after the last edit, where before they scanned an earlier draft and never looked again. (Still optional: no Python, no checker, in both passes.)
- References load at the step that needs them instead of all at once.

### Fixed
- **The checker no longer flags valid frontmatter.** A `>`-folded or `|`-block description, or a list-valued field, used to be reported as unreadable *and* as "description too short" — with the description quoted as `>-`. It now reads all three, and never derives a second finding from a value it couldn't read.
- **The checker stopped calling product names secrets.** A catch-all "long mixed-case string" rule fired on ordinary taglines and then redacted the evidence, so nobody could tell a leaked key from a headline. The vendor-prefix patterns that find real keys are unchanged.
- Removed a false claim in the skill template that a folded `>` description won't parse. It parses.
- Removed a block in create-skill that invented a base-directory variable and a fake install path. Followed literally it pointed the checker at a file that doesn't exist, so the check quietly never ran.
- create-skill and tidy-skill now say what to do when a helper subagent isn't available, instead of leaving no legal way to finish. tidy-skill's release gate previously forbade both the check and the way out.
- The product-brief working notes (`brief.md`, `research.md`, `feasibility.md`) no longer ship to students.

## 0.2.0 — 2026-07-23

- Added **tidy-skill**: cleans up a skill that works but reads badly, without changing what it does — and proves behavior survived by running old and new versions in separate fresh contexts.

## 0.1.0 — 2026-07-04

- First release: **create-skill** and **improve-skill**.
