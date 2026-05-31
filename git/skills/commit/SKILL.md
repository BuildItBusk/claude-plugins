---
name: commit
description: Commit code changes to local git repository, following the user's preferences
argument-hint: optional context for commit message
allowed-tools: Bash(git *)
---

# Git Commit Skill

Stage and commit changes to local git repository, following the preferences described below.

## Granularity

- Split changes into multiple commits when they are logically separate.
- Each commit should be a coherent, self-contained unit of work — don't commit a change mid-refactor that leaves the tree broken.
- Ignore changes not related to the current work, but notify the user when you do.

## Commit Message Conventions

- Always have a clear, concise summary line starting with a capital letter and using imperative mood.
- If the change needs context, add a bulleted list after a blank line, explaining concisely what changed
- Include a _why_ for the change, if it's not obvious, but keep it brief
- Omit any information which is not useful to a future reader (e.g. "Co-authored by Claude" typically does not provide any value)