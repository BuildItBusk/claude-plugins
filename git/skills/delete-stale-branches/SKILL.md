---
name: delete-stale-branches
description: Delete local stale branches, which have already been deleted from the origin.
allowed-tools: Bash(git fetch:*), Bash(git status), Bash(git branch:*), Bash(git log:*), Bash(git diff:*), Bash(git show:*), Bash(git remote:*), Bash(git for-each-ref:*), Bash(git rev-parse:*), Bash(git merge-base:*), Bash(git stash list), Bash(git symbolic-ref:*)
disable-model-invocation: true
---

# Delete Stale Branches

Clean up local branches that are no longer needed.

## Procedure

1. **Detect default branch:** Run `git symbolic-ref refs/remotes/origin/HEAD` to determine the default branch (e.g. `main` or `master`). Use this as the base for all merge and age comparisons below.
2. **Sync with remote:** Run `git fetch --prune` to update remote tracking info
3. **Identify current branch:** Never delete the currently checked-out branch
4. **Categorize branches** using the tiers below
5. **Delete Tier 1 branches** without asking
6. **Present Tier 2 branches** and ask for confirmation before deleting
7. **Report Tier 3 branches** but do not offer to delete

## Deletion Tiers

### Tier 1: Auto-delete (no permission needed)
- Fully merged into the default branch (`git branch --merged <default>`)

### Tier 2: Ask permission first
- Remote deleted (`[gone]`) but has commits not in the default branch
- No remote tracking AND no unique commits (orphaned empty branches)
- Last commit > 3 months old AND behind the default branch
- No remote tracking AND last commit > 1 month old

### Tier 3: Report only (do not delete)
- Has commits not in the default branch (unmerged work)
- Less than 1 month old with no remote

## Safety Rules

- Use `git branch -d` (safe delete) for merged branches
- Use `git branch -D` (force delete) only for Tier 1 `[gone]` branches
- Never delete the default branch or `release/*` branches
- If a branch has uncommitted changes, warn and skip
- Always show what was deleted at the end

## Output Format

```
Deleted (auto):
  - dev/jbsn/old-feature [gone]
  - dev/jbsn/merged-fix [merged]

Deleted (confirmed):
  - dev/jbsn/abandoned-work [3 months old, no remote]

Skipped:
  - dev/jbsn/active-work [has unmerged commits]
```
