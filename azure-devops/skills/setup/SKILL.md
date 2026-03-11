---
name: setup-azure-devops
description: Create or update the .azure-devops.json config file for this repository
disable-model-invocation: true
allowed-tools: Bash(python *detect_ado_remote.py*), Write, Read
---

# Instructions

1. **Detect remote** by running:
   ```
   python ${CLAUDE_SKILL_DIR}/detect_ado_remote.py
   ```
2. If `.azure-devops.json` already exists in the repo root, read it and show the current values
3. Using the detected output, pre-fill what was found (org, project, repository, default_branch)
4. For any value that is empty or could not be detected, ask the user
5. Show the final config and ask the user to confirm
6. Write `.azure-devops.json` to the repo root
