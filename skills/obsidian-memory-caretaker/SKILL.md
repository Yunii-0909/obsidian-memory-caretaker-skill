---
name: obsidian-memory-caretaker
description: Search and maintain an Obsidian work knowledge base as long-term memory. Use when a task may depend on prior project rules, operating procedures, personal preferences, historical decisions, meeting outcomes, scripts, Feishu/Base/SQL workflows, KPI/reporting logic, team-management context, or when a conversation creates new reusable knowledge that should be written back to Obsidian.
---

# Obsidian Memory Caretaker

## Purpose

Act as a long-term work-memory caretaker. Before doing knowledge-dependent work, search the Obsidian vault for prior experience. After meaningful discussions or completed work, decide whether new reusable knowledge should be written back.

Default vault resolution:

```text
1. $OBSIDIAN_VAULT_PATH
2. the nearest current working directory that looks like an Obsidian vault
3. ask the user for the vault path
```

## Core Workflow

### 1. Pre-task memory scan

Run this when the user asks for work involving projects, data, processes, people, tools, reports, schedules, KPI, content distribution, meetings, or anything likely to have prior context.

1. Extract 3-8 search terms from the request: project names, people, platform names, table names, deliverable names, dates, and business terms.
2. Search the vault with `scripts/search_obsidian.py` or `rg`. Pass `--vault` when `OBSIDIAN_VAULT_PATH` is not set.
3. Read only the most relevant notes.
4. Use prior rules and decisions in the task.
5. If no relevant notes are found, say so briefly only when it matters.

Example:

```bash
OBSIDIAN_VAULT_PATH="/path/to/Obsidian/Vault" python scripts/search_obsidian.py "weekly report rules"
```

### 2. During-task memory awareness

Prefer existing knowledge over improvising:

- Use documented data口径, field mappings, scripts, and reporting structures.
- Respect prior management decisions and pending confirmations.
- Treat documents marked "待确认" as provisional.
- Do not overwrite established rules unless the user explicitly says the rule changed.

### 3. Post-task memory capture

At natural stopping points, decide whether to write back.

Write to Obsidian when the conversation creates:

- a new confirmed rule or口径
- a project strategy or management decision
- a repeatable workflow
- a tool/API connection method
- a known pitfall and fix
- a recurring schedule or operating rhythm
- a person/team context that affects future decisions
- a task handoff or SOP

Do not write:

- fleeting emotions with no future task relevance
- secrets, tokens, passwords, private keys, or full credentials
- raw chat transcripts
- unconfirmed speculation as fact
- duplicate summaries that add no future value

Read `references/memory_policy.md` when judging whether something deserves to be saved.

## Write-back Rules

1. Search first for an existing note to update.
2. Prefer appending a dated section to the most relevant existing note.
3. Create a new note only when no suitable note exists.
4. Mark uncertain items with `待确认`.
5. Preserve sensitive boundaries: describe connection methods without storing secrets.
6. Keep entries short, operational, and future-facing.
7. Include source/date in a light form, such as `记录时间：2026-06-09` or `来源：与用户讨论确认`.

Read `references/routing.md` before creating or moving notes.

## Suggested Note Shape

For small updates:

```markdown
## YYYY-MM-DD 更新

- 结论：
- 影响：
- 后续：
```

For bigger updates, use the templates in `references/templates.md`.

## Conflict Handling

If a new statement conflicts with an existing note:

1. Do not silently replace the old rule.
2. Add a dated update explaining the change if the user clearly confirmed it.
3. If not confirmed, add `待确认` or ask one concise question.

## User-Facing Behavior

Be quiet but transparent:

- Mention the scan when it affects the answer: "我先看了知识库里的周报口径..."
- Mention write-back after saving: "我也把这条规则补进知识库了。"
- Do not ask for permission for every small operational update if the user has asked for automatic knowledge maintenance.
- Ask before saving sensitive personal content or ambiguous emotional context.
