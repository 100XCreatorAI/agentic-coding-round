---
name: problem
description: Understand the problem statement in PROBLEM.md, discuss it with the user, and write plan.md. Planning only — never writes code. Use at the start of the round or when the problem changes.
---

# /problem — understand and plan

**Do not write or edit any code in this skill.** The only file you may write is `plan.md`, and only after the user agrees.

## Step 1 — Read
Read `PROBLEM.md`. If it is empty, ask the user to paste the problem statement there and stop.

## Step 2 — Restate
In plain words, tell the user:
- **What** we are building (one or two sentences)
- **Inputs** and **outputs**
- **Constraints** (time, performance, libraries, format, limits)
- **Hidden requirements** — things implied but not stated

## Step 3 — Ask
List every ambiguity as a numbered question. Suggest a sensible default for each.
**Stop and wait for the user's answers.**

## Step 4 — Approaches
Propose 2–3 approaches. For each: how it works, complexity, time to build, risk.
Recommend one and say why. **Wait for the user to agree.**

## Step 5 — Write plan.md
Fill in `plan.md` using its template:
- Goal, chosen approach
- Milestones: small, ordered, each testable on its own
- "Done when" checklist
- Known edge cases (these feed `/test`)
- Open questions / assumptions

Show the user the final plan and ask if anything should change.
