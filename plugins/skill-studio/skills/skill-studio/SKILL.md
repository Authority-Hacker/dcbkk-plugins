---
name: skill-studio
description: Use when making repeated work reusable, teaching the assistant from a task or corrections, or sorting out an existing skill without a chosen lane, such as "help with this and remember how I like it" or "make this repeatable". Does the task, then creates, updates, repairs or tidies the relevant skill. A one-off output edit with no request to reuse it is excluded; explicit create-skill, improve-skill and tidy-skill requests can go directly to those specialists.
---

# Skill Studio

Help the person get useful work done and carry the way they like it into the next task. Choose the route from the actual request, then follow it; don't stop at recommending a skill.

| Situation | Route |
| --- | --- |
| A task to do now, with preferences still forming in the task, examples or corrections | Read [learn from work](references/learn-from-work.md) now and nothing else until they accept the work; it then hands on to create-skill, which asks why where it matters. |
| A new skill with a usable brief, established rules or accepted work | Invoke [create-skill](../create-skill/SKILL.md) |
| An existing skill should change a lasting preference ("always put the date first") | Invoke [improve-skill](../improve-skill/SKILL.md) |
| An existing skill gives wrong output, misses promised behavior, never fires, or needs putting back | Invoke [improve-skill](../improve-skill/SKILL.md) |
| A skill that has grown messy, repetitive or self-contradicting after lots of changes | Invoke [tidy-skill](../tidy-skill/SKILL.md) |

The complaint wins over the words. A skill that gives a specific wrong output needs improve-skill even when they say "tidy"; a skill that's "a mess" or "contradicts itself", with no specific wrong output, needs tidy-skill even when they say "fix". Ask one focused question only if the context can't tell the routes apart. Once the route is clear, hand over before asking the person anything else: the specialist decides what to ask. Invoke the specialist through the host's skill mechanism when supported; otherwise read the selected file and follow it.

Carry forward the request, the exact skill, real input and accepted output, corrections, and earlier approvals, so the specialist resumes the same job rather than restarting it.
