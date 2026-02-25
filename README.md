# claude-plugins

Personal Claude Code plugins by Jakob Busk Sørensen.

## Installation

> All `/plugin` commands are run inside Claude Code, not in a terminal.

Add the marketplace (one-time setup):

```
/plugin marketplace add https://github.com/BuildItBusk/claude-plugins
```

Then install individual plugins:

```
/plugin install code-review@BuildItBusk-plugins
/plugin install git@BuildItBusk-plugins
```

Alternatively, run `/plugin` to open the interactive UI and browse from there.

## Plugins

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

```
<plugin-name>/
  .claude-plugin/
    plugin.json       # name, description, version
  skills/
    <skill-name>/
      SKILL.md        # skill instructions and frontmatter
```
