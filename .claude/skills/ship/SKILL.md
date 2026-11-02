---
name: ship
description: Git pull, then preview exactly what will be committed and pushed, wait for the user's "go ahead", then commit with the exact message, push, and open a PR. Only run when the user invokes /ship.
argument-hint: "[optional commit message or branch name]"
disable-model-invocation: true
---

# /ship — pull, preview, wait, push

**Never commit or push before the user explicitly says "go ahead" (or similar) in reply to the preview.**

## Step 1 — Sync
```bash
git fetch && git status -sb
```
If on `main`, create a feature branch: `feature/<short-kebab-name>` (or use the name in `$ARGUMENTS`).
Pull the latest: `git pull --rebase origin main`. If there are conflicts, stop and show them.

## Step 2 — Safety checks (public repo)
- No `.env`, keys, tokens, or passwords in the changes (`git diff` + untracked files).
- No junk: `__pycache__`, `.pytest_cache`, `.DS_Store`, large files.
- Tests pass: `pytest -q`. If they fail, report and ask whether to continue.

## Step 3 — Preview (then STOP)
Show the user exactly this:

```
Branch:   feature/...
Files:
  A  path/new_file.py
  M  path/changed_file.py
  D  path/deleted_file.py
Diff:     <short summary of what changed, per file>
Tests:    ✅ N passed
Secrets:  ✅ none found

Commit message (exact):
  feat: <short summary>

  <optional body: what and why>

PR: will open against main — yes/no
```
Use conventional commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`.

Ask: **"Go ahead?"** and **stop. Wait for the user's reply.**

## Step 4 — Respond to the user
- **"go ahead"** → continue to Step 5.
- Changes requested (message, files, branch) → apply them and show the preview again.
- **"no"/"cancel"** → stop; change nothing.

## Step 5 — Commit and push
Stage only the files listed in the preview (by name — not `git add -A`), commit with the exact approved message, then:
```bash
git push -u origin <branch>
```
If the user wanted a PR: `gh pr create --base main --title "<commit subject>" --body "<summary + test results>"`.

## Step 6 — Confirm
Report the commit hash, branch, and PR URL. Show `git status -sb` to prove the tree is clean.
