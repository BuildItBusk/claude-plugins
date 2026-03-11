---
name: setup-azure-devops
description: Create or update the .azure-devops.json config file for this repository
disable-model-invocation: true
allowed-tools: Bash(python ${CLAUDE_SKILL_DIR}/detect_ado_remote.py*), Write, Read
---

# Detected remote

```json
!`python ${CLAUDE_SKILL_DIR}/detect_ado_remote.py`
```

# Instructions

1. If `.azure-devops.json` already exists in the repo root, read it and show the current values
2. Using the detected remote above, pre-fill what was found (org, project, repository, default_branch)
3. For any value that is empty or could not be detected, ask the user
4. Show the final config and ask the user to confirm
5. Write `.azure-devops.json` to the repo root
