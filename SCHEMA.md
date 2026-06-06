# Output Schema

> 仓库规范与命名约定。所有文档遵循此规范。

## Directory Structure

```
hermes-output/
├── README.md           # 仓库说明
├── SCHEMA.md           # 本文件：规范、约定
├── index.md            # 总索引（所有文档目录）
├── log.md              # 操作日志（append-only）
├── guides/             # 教程、操作指南、how-to
├── notes/              # 笔记、配置记录、调试过程
├── research/           # 调研报告（深度分析、技术选型）
├── reports/            # 定期报告（日报、周报、trending）
├── plans/              # 规划、路线图
├── scripts/            # 脚本文件
├── references/         # 常用资料、速查表
└── archive/            # 历史存档（过期内容）
```

## Naming Conventions

### File Names
- 格式：`YYYY-MM-DD-kebab-case-title.md`
- 日期前缀：所有带时间属性的文档必须带日期
- 无日期文档：纯知识性内容可不带日期（如 `codex-cli-guide.md`）
- 语言：文件名用英文，内容可用中文
- 禁止：空格、中文文件名、特殊字符

### Examples
```
✅ 2026-06-05-github-trending.md
✅ codex-cli-guide.md
✅ 2026-05-29-git-ssh-dns-vpn-fix.md
❌ GitHub Trending 日报.md
❌ 2026/06/05-report.md
```

## Frontmatter

每个文档建议带 YAML frontmatter：

```yaml
---
title: 文档标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: guide | note | research | report | plan | reference
tags: [tag1, tag2]
summary: 一句话摘要
---
```

## Tag Taxonomy

### Content Type
- `guide` - 教程、操作指南
- `note` - 笔记、备忘
- `research` - 调研报告
- `report` - 定期报告
- `plan` - 规划
- `reference` - 速查资料

### Domain Tags
- `hermes` - Hermes Agent 相关
- `gitlab` - GitLab / CI/CD
- `github` - GitHub 相关
- `ai` - AI / LLM / 模型
- `devops` - 运维、部署
- `trade` - 外贸、跨境
- `tool` - 工具使用
- `config` - 配置记录
- `debug` - 调试记录

## Directory Rules

### guides/
- 完整的操作步骤
- 可复现的流程
- 包含验证方法

### notes/
- 配置变更记录
- 问题排查过程
- 不要求完整性，重在记录

### research/
- 有明确的调研目标
- 包含结论和建议
- 可引用外部资料

### reports/
- 定期生成的内容
- 格式相对固定
- 时效性较强

### plans/
- 未来规划
- 路线图
- 里程碑

### scripts/
- 可执行脚本
- 自动化工具
- 需附带使用说明

### references/
- API 文档速查
- 命令参考
- 配置模板

### archive/
- 过期内容
- 已完成的项目文档
- 不再维护的资料

## Operations

### Adding New Content
1. 确定内容类型 → 选择目录
2. 按命名规范命名文件
3. 添加 frontmatter
4. 更新 `index.md`
5. 追加 `log.md`

### Archiving
1. 移动到 `archive/`
2. 保留原始路径（如 `archive/guides/old-guide.md`）
3. 从 `index.md` 移除或标记 archived
4. 记录到 `log.md`
