# BuildItBusk's Claude Code Plugins

My personal Claude Code tools which are not project specific. They are optimized to my personal use, but I made the repository public, in case they can help or inspire others.

## Installation

> All `/plugin` commands are run inside Claude Code, not in a terminal.

Add the marketplace (one-time setup):

```sh
/plugin marketplace add https://github.com/BuildItBusk/claude-plugins
```

Then install individual plugins:

```sh
/plugin install azure-devops@BuildItBusk-plugins
/plugin install code-review@BuildItBusk-plugins
/plugin install git@BuildItBusk-plugins
```

Alternatively, run `/plugin` to open the interactive UI and browse from there.

## Plugins

### `azure-devops`

Skills for Azure DevOps workflows. Requires a `.azure-devops.json` file in the repository root:

```json
{
  "org": "myorg",
  "project": "myproject",
  "repository": "myrepo",
  "default_branch": "main"
}
```

`default_branch` is optional and defaults to `main`. The other three fields are required. This file can safely be committed — it contains no secrets. Run `/setup-azure-devops` to create it automatically — it detects values from your git remote.

| Skill | Usage | Description |
|-------|-------|-------------|
| `setup-azure-devops` | `/setup-azure-devops` | Creates `.azure-devops.json` by detecting org/project/repo from the git remote. Asks for confirmation and fills in anything it can't detect. |
| `create-pr` | `/create-pr [title]` | Creates a pull request for the current branch. Derives title and description from commits and diff stat, pushes the branch if needed, and opens the PR in your browser. |

### `code-review`

Skills for reviewing diffs.

| Skill | Usage | Description |
|-------|-------|-------------|
| `diff-review` | `/diff-review [branch]` | Diffs a branch against the default branch and reports bugs, security issues, and CLAUDE.md violations. Escalates low-confidence findings to Opus for verification. Defaults to the current branch if no argument is given. |

### `git`

Skills for common git workflows.

| Skill | Usage | Description |
|-------|-------|-------------|
| `commit` | `/commit [context]` | Stages changes, drafts a commit message, and commits. Suggests running tests when source files are changed. Handles untracked files with a recommendation rather than blindly staging everything. |
| `delete-stale-branches` | `/delete-stale-branches` | ⚠️ Cleans up local branches that are no longer needed. Auto-deletes merged branches, asks before deleting stale or gone branches with unmerged work, and reports branches with active work. |

## Structure

Each plugin lives in its own directory and follows the standard Claude Code plugin layout:

```sh
<plugin-name>/
  .claude-plugin/
    plugin.json       # name, description, version
  skills/
    <skill-name>/
      SKILL.md        # skill instructions and front-matter
```
