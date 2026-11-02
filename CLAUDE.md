# Agentic Coding Round — rules for Claude

## Source of truth
- `PROBLEM.md` — the problem statement (pasted by the user). Read it before any work.
- `plan.md` — the agreed plan. Follow it step by step. If something is not in the plan, ask before doing it.

## Workflow
1. `/problem` — understand the problem and write `plan.md`. No code in this step.
2. Build one milestone from `plan.md` at a time.
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
