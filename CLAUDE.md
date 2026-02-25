# CLAUDE.md

## Overview

This repository is a Claude Code **plugin marketplace** — a catalog of plugins that can be installed into Claude Code. It can be used locally or added directly from GitHub.

## Structure

```
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
```shell
/plugin validate .
```

Test locally end-to-end:
```shell
/plugin marketplace add ./
/plugin install <plugin-name>@plugins
```