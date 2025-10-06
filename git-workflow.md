# Git Workflow - Avoiding Merge Conflicts

## Simple 3-Step Workflow (Do this EVERY time):

### Before making changes:
```powershell
# 1. Always pull first
git pull origin main

# 2. Make your changes (add files, edit code, etc.)

# 3. Then add, commit, and push
git add .
git commit -m "Your commit message"
git push origin main
```

## If you get a "fetch first" error:

### Option 1: Simple merge (recommended for solo projects)
```powershell
git pull origin main
# Resolve any conflicts if they appear
git push origin main
```

### Option 2: If you want to keep your changes on top
```powershell
git pull --rebase origin main
# Resolve any conflicts if they appear
git push origin main
```

## Quick Status Check Commands:
```powershell
git status                    # See what's changed locally
git log --oneline -5         # See recent commits
git remote -v                # Check your remote URL
```

## Emergency: If things get too messy
```powershell
# This will reset to match the remote exactly (CAREFUL: loses local changes)
git fetch origin
git reset --hard origin/main
```

## Pro Tip:
Always run `git pull origin main` before starting work on your code!