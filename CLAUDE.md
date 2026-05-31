# CLAUDE.md

## Overview

This repository is my personal Claude Code **plugin marketplace** - it contains the Claude Code tools I use, which are not project specific.

## Source control

The repository is tracked in a public Github repository at <https://github.com/BuildItBusk/claude-plugins>.

## Structure

```sh
claude-plugins/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog (name, owner, plugin list)
├── code-review/                  # "code-review" plugin
│   ├── .claude-plugin/
│   │   └── plugin.json           # Plugin manifest (name, description, version)
│   └── skills/
│       └── diff-review/
│           └── SKILL.md          # /diff-review skill definition
├── git/                          # "git" plugin
│   ├── .claude-plugin/
│   │   └── plugin.json           # Plugin manifest (name, description, version)
│   └── skills/
│       └── commit/
│           └── SKILL.md          # /commit skill definition
├── azure-devops/                 # "azure-devops" plugin
│   ├── .claude-plugin/
│   │   └── plugin.json           # Plugin manifest
│   └── skills/
│       ├── create-pr/
│       │   └── SKILL.md          # /create-pr skill definition
│       └── setup/
│           └── SKILL.md          # /setup-azure-devops skill definition
├── CLAUDE.md
└── README.md
```

Each plugin lives in its own top-level directory and follows the same layout: a `.claude-plugin/plugin.json` manifest and a `skills/` directory containing one subdirectory per skill, each with a `SKILL.md` file. The root `.claude-plugin/marketplace.json` references all plugins by their relative paths.

## Adding a plugin

1. Create a top-level directory for the plugin (kebab-case name).
2. Add `.claude-plugin/plugin.json` with `name`, `description`, and `version`.
3. Add one `skills/<skill-name>/SKILL.md` per skill the plugin provides.
4. Register the plugin in `.claude-plugin/marketplace.json` under `plugins`, with `"source": "./<plugin-dir>"`.
5. When modifying an existing plugin, bump `version` in its `plugin.json` — Claude Code uses this to detect updates.

## Validating and testing

Validate the marketplace structure:

```sh
/plugin validate .
```

Test locally end-to-end:

```sh
/plugin marketplace add ./
/plugin install <plugin-name>@plugins
```

## References

Read the references when working on **non-trivial** things in any of the referenced topics.

- [Claude Memories](https://code.claude.com/docs/en/memory.md) - How to use `CLAUDE.md` files and auto memory
- [Claude Code Skills](https://code.claude.com/docs/en/skills.md) - Instructions and best practices on writing skills for Claude Code
- [Claude Code Plugins](https://code.claude.com/docs/en/plugins) - Creating and sharing plugins for Claude Code
