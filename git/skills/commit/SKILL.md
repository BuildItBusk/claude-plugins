---
name: commit
description: Create a git commit following good commit conventions
argument-hint: optional context for commit message
allowed-tools: Bash(git diff:*), Bash(git add:*), Bash(git status), Bash(git log:*), Bash(git branch:*), Bash(git symbolic-ref:*), Bash(dotnet test:*), Bash(npm test), Bash(pytest:*), Bash(make test)
---

# Prerequisites

Detect the default branch by running `git symbolic-ref refs/remotes/origin/HEAD`. If the current branch is the default branch (typically `main` or `master`), warn the user and ask them to confirm before proceeding.

# Instructions
1. **Analysis:** Check `git status` and `git diff`.
2. **Tests:** If the diff contains changes to source code files (not just scripts, config, docs, or Markdown), suggest running tests before committing. Use judgment — if the change is trivial (a typo fix, a comment, a version bump) or only touches non-code files, skip this. If tests seem relevant, detect the test runner from the repo (e.g. `dotnet`, `npm test`, `pytest`, `make test`) and ask the user if they'd like to run them.
3. **Stage:**
   - Run `git add -u` to stage modifications and deletions to tracked files.
   - If `git status` shows untracked files, recommend which ones to stage based on
     context (e.g. source files related to the diff, new test files). Exclude files
     that look like build artifacts, secrets, or editor noise. Present the
     recommendation and ask the user to confirm or adjust before staging them.
4. **Draft Message:** Create a commit message following these conventions:
    - Start with a capital letter
    - Use imperative mood: "Fix bug" (not "Fixed bug")
    - Keep summary line under 50 characters
    - Add explanation on separate lines when the change needs context:
        - Why the change was made
        - Technical decisions or trade-offs
        - Impact on other parts of the system
    - For multi-line commits, use multiple -m flags: `git commit -m "Summary" -m "" -m "- Detail 1" -m "- Detail 2"`
    - The second -m with empty string creates the required blank line between summary and body.
    - Only use multi-line commits if the extra lines significantly increase clarity.
        - Don't need explanation: "Fix typo", "Update dependency version", "Add missing semicolon"
        - Do need explanation: Architectural decisions, non-obvious bug fixes, trade-offs, breaking changes
    - Only add information which provides value. E.g. "Co-authored by Claude" does not provide any value
5. **Commit:** Run `git commit -m "[message]"`.