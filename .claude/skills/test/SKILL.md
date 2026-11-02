---
name: test
description: Step-by-step edge-case testing with pytest. Builds an edge-case checklist, writes tests, runs them, reports results, and fixes failures. Use after building a milestone or when asked to test code.
argument-hint: "[file or function to test — defaults to recent changes]"
---

# /test — edge-case testing, step by step

Target: `$ARGUMENTS` (if empty, test the files changed since the last commit — `git diff --name-only HEAD` plus untracked files in `src/`).

## Step 1 — Understand
Read the target code, `plan.md` (especially "Known edge cases"), and existing tests in `tests/`.
Summarise in 2–3 lines what the code should do.

## Step 2 — Edge-case checklist
Build a checklist before writing any test. Cover every category that applies:

| Category | Examples |
|---|---|
| Happy path | typical valid input |
| Empty / missing | `""`, `[]`, `{}`, `None`, missing keys/args |
| Boundaries | 0, 1, -1, max/min, off-by-one, single element |
| Types / malformed | wrong type, bad format, invalid JSON, NaN |
| Size / performance | very large input, deep nesting, timing |
| Data quirks | duplicates, ordering, unicode, whitespace, case |
| Errors | expected exceptions and their messages |
| External deps | missing env vars, API/network failure, file not found (mock these) |
| State | repeated calls, idempotency, side effects |

**Show the checklist to the user** before writing tests.

## Step 3 — Write tests
- Write them in `tests/test_<module>.py`, grouped by category with clear names (`test_empty_input_returns_empty_list`).
- Use `pytest.mark.parametrize` for input variants and `pytest.raises` for errors.
- Mock external services; never call real APIs or use real keys.

## Step 4 — Run
```bash
source .venv/bin/activate && pytest -v
```

## Step 5 — Report
Give a results table: case · category · ✅/❌ · reason for failure.

## Step 6 — Fix loop
For each failure, decide: **bug in code** or **bug in test**?
- Bug in the test → fix the test.
- Bug in the code → explain it, fix it, and re-run.
- If the expected behaviour is unclear, ask the user rather than guess.

Repeat Steps 4–6 until everything is green. Finish with: total tests, passed, edge cases covered, and anything left untested.
