# Obsidian Memory Caretaker Skill

A Codex Skill that helps agents use an Obsidian vault as long-term work memory.

It teaches an agent to:

- search existing Obsidian notes before doing knowledge-dependent work
- respect prior rules, project context, reporting logic, decisions, and workflows
- decide whether new reusable knowledge should be written back
- avoid storing secrets, raw chat logs, and low-value noise

## Install

Install from this repository with the Codex skill installer:

```bash
python /path/to/install-skill-from-github.py \
  --repo Yunii-0909/obsidian-memory-caretaker-skill \
  --path skills/obsidian-memory-caretaker
```

Restart Codex after installing.

## Configure Your Vault

Set your Obsidian vault path:

```bash
export OBSIDIAN_VAULT_PATH="/path/to/your/Obsidian/Vault"
```

You can also pass a vault path directly to the bundled search script:

```bash
~/.codex/skills/obsidian-memory-caretaker/scripts/search_obsidian.py \
  "weekly report KPI rules" \
  --vault "/path/to/your/Obsidian/Vault"
```

## Skill Contents

```text
skills/obsidian-memory-caretaker/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── memory_policy.md
│   ├── routing.md
│   └── templates.md
└── scripts/
    └── search_obsidian.py
```

## Notes

This skill does not include any private vault content. It only provides the workflow, policies, templates, and a local search helper.
