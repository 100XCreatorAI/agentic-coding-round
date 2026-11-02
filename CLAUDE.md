# Agentic Coding Round — rules for Claude

## Source of truth
- `plan.md` — the user's plan. **Implement exactly what it says, nothing more.** Do not design, replan, or add features. If a step is unclear or missing, ask the user before doing anything.
- `PROBLEM.md` — the problem statement (pasted by the user). Context only; it never overrides `plan.md`.

## Workflow
1. User fills in `plan.md` (and `PROBLEM.md`).
2. Implement one milestone from `plan.md` at a time, in the most optimised way the plan allows.
3. `/test` — edge-case test the milestone.
4. Run the `plan-guardian` agent in the background to review plan adherence and optimisation.
5. `/ship` — preview the commit, wait for the user's "go ahead", then push.

## Rules
- Never push or commit without the user's explicit approval via `/ship`.
- Never commit `.env`, API keys, or secrets. This repo is **public**.
- Keep code simple and readable; small, focused commits.
- Tick off milestones in `plan.md` as they are completed.

## Project
- Python, venv at `.venv/` (`source .venv/bin/activate`).
- Run: `python -m src.main` · Test: `pytest -v`
- Code in `src/`, tests in `tests/`.
