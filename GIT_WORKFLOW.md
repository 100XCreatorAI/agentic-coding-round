# Git workflow (terminal)

```bash
cd ~/agentic-coding-round && source .venv/bin/activate

git pull                          # get latest
git checkout -b feature/my-change # new branch
git add -A && git commit -m "msg" # commit
git push -u origin feature/my-change

# merge into main
git checkout main && git pull
git merge --no-ff feature/my-change
git push
git branch -d feature/my-change

git status -sb                    # should show: ## main...origin/main (clean)
```
