# Vault Routing

Vault path:

```text
$OBSIDIAN_VAULT_PATH
```

If the environment variable is not set, ask the user for the path or infer it from the current workspace only when obvious.

## Directory Map

Use existing structure when possible.

| Content | Preferred Location |
|---|---|
| Team management, salary, promotion, handoff, attribution | `20_团队管理/` |
| Project strategy and operating decisions | relevant project folder, or `10_项目管理/` if present |
| Data sync, SQL, Feishu/Base, report automation | `30_数据分析与同步/` |
| Tool/API/MCP/CLI/hardware usage | `40_工具自动化/` |
| Communication logs, assistant continuity notes | `50_日志与通信/` |
| Weekly/monthly reports | keep existing report workflow; do not restructure unless asked |
| Content distribution/GEO | existing GEO or content distribution folders |

## Search Before Writing

Before creating a note, search:

```bash
rg -n "keyword1|keyword2" "$OBSIDIAN_VAULT_PATH"
```

Prefer updating an existing note if it already owns the topic.

## Filename Rules

- Use Chinese business names when they are the user's normal terms.
- Avoid vague filenames like `总结.md`.
- Include project/tool/person when useful.
- Do not create many tiny notes for one topic; append dated sections.

## Link Rules

When adding references, use Obsidian wikilinks if the target is inside the vault:

```markdown
[[20_团队管理/运营业绩归因规则]]
```

Use plain URLs only for external systems.
