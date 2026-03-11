---
name: create-pr
description: Create an Azure DevOps pull request for the current branch
argument-hint: "[title]"
disable-model-invocation: true
allowed-tools: Bash(python ${CLAUDE_SKILL_DIR}/pr_context.py*), Bash(python ${CLAUDE_SKILL_DIR}/pr_create.py*)
---

# Instructions

1. **Gather context** by running:
   ```
   python ${CLAUDE_SKILL_DIR}/pr_context.py
   ```
2. **Draft title and description** from the output (commits and diff stat):
   - If the user provided a title via `$ARGUMENTS`, use it
   - Otherwise, derive a concise title from the commit messages
   - Write a short description — what changed and why, no filler
   - If commits reference work item IDs (`#12345` or `AB#12345`), include them
3. **Show the user** the title, description, and target branch — ask to confirm or adjust
4. **Create the PR** (handles push + `az repos pr create` using `.azure-devops.json`):
   ```
   python ${CLAUDE_SKILL_DIR}/pr_create.py "<title>" "<description>" [target-branch]
   ```
   Target branch is optional — defaults to the value in `.azure-devops.json`.
5. **Output** the PR URL
