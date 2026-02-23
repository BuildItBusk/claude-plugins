---
name: review
description: Compare a branch to the default branch and code review the changes
argument-hint: optional branch name
allowed-tools: Read, Grep, Glob, Bash(git diff:*), Bash(git status), Bash(git fetch:*), Bash(git log:*), Bash(git checkout:*), Bash(git stash:*), Bash(git symbolic-ref:*)
---

# Assumptions
- If no branch name is provided through the argument, assume that it is the current branch which needs reviewed
- Detect the default branch by running `git symbolic-ref refs/remotes/origin/HEAD`
- If no branch argument is provided and the current branch is the default branch, warn the user and stop — there is nothing to diff

# Preparation
1. **Sync:** Fetch the default branch (e.g. `git fetch origin main`)
2. **Switch to branch:** If a branch name is provided through the argument:
   - Check for uncommitted changes with `git status`
   - If there are uncommitted changes, stash them before checkout
   - Run `git checkout {branch-name}`
   - Restore stashed changes if any were stashed
3. **Gather context:**
   - Run `git status` to see all changes (staged, unstaged, untracked)
   - Run `git log {default-branch}..HEAD --oneline` to see committed changes (if any)
   - Run `git diff {default-branch} --stat` to see files changed summary (includes uncommitted)
   - Run `git diff {default-branch}` to get full diff for review (includes uncommitted)
   - For untracked files shown in status, read them with Read tool to review their contents
4. Sonnet reviews diff for HIGH SIGNAL issues only:
   - **Bugs:** Code that will fail to compile, clear logic errors, definite wrong results
   - **Security:** Injection vulnerabilities, hardcoded secrets, authentication issues
   - **CLAUDE.md violations:** Clear violations you can quote from CLAUDE.md

   Confidence levels:
   - HIGH: Definite issue (syntax error, clear logic bug, explicit CLAUDE.md violation)
   - LOW: Uncertain or depends on broader context

   Do NOT flag: style/quality concerns, potential issues depending on inputs, pre-existing issues

   Ignore (these are false positives):
   - Pre-existing issues not introduced in this diff
   - Pedantic nitpicks a senior engineer wouldn't flag
   - Issues a linter will catch
   - Style/quality concerns unless required by CLAUDE.md

5. For each LOW confidence issue: spawn Opus to verify
   - Use Read tool to view full file context if needed
   - Provide: the issue description, relevant diff context, CLAUDE.md
   - Ask: "Is this actually a problem? Respond: confirmed, dismissed, or uncertain"

6. Output findings:

   ## Critical Issues
   - file:line - Description of issue

   ## Warnings
   - file:line - Description of issue

   ## Summary
   X files reviewed, Y issues found

   Include all high-confidence issues from Sonnet and confirmed issues from Opus verification
7. **Optional validation:** If significant logic changes exist, suggest running the project's test suite to verify functionality
