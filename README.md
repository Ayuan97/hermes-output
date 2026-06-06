# Hermes Output

> Hermes Agent 的输出仓库，用于持久化一切有价值的产出。

## Quick Start

- **找文档？** → 看 [index.md](index.md)
- **了解仓库目的？** → 看 [purpose.md](purpose.md)
- **看全局概况？** → 看 [overview.md](overview.md)
- **写新文档？** → 看 [SCHEMA.md](SCHEMA.md) 的命名规范
- **看历史操作？** → 看 [log.md](log.md)

## Directory Structure

```
hermes-output/
├── README.md           # 本文件
├── SCHEMA.md           # 规范、命名约定
├── purpose.md          # 仓库目的、研究范围
├── index.md            # 文档总索引
├── overview.md         # 全局摘要（自动更新）
├── log.md              # 操作日志
├── guides/             # 教程、操作指南
├── notes/              # 笔记、配置记录
├── research/           # 调研报告
├── reports/            # 定期报告（日报、周报）
├── synthesis/          # 跨主题综合分析
├── plans/              # 规划、路线图
├── scripts/            # 脚本工具
├── references/         # 常用资料
└── archive/            # 历史存档
```

## Naming Convention

- 日期文档：`YYYY-MM-DD-kebab-case-title.md`
- 纯知识文档：`kebab-case-title.md`
- 文件名用英文，内容可用中文

## Quick Reference

| 类型 | 目录 | 说明 |
|------|------|------|
| 操作指南 | guides/ | 可复现的步骤流程 |
| 调试记录 | notes/ | 配置变更、问题排查 |
| 深度调研 | research/ | 有结论的调研报告 |
| 定期产出 | reports/ | 日报、周报、trending |
| 综合分析 | synthesis/ | 跨主题汇总、对比研究 |
| 未来规划 | plans/ | 路线图、里程碑 |
| 脚本工具 | scripts/ | 可执行文件 |
| 速查资料 | references/ | API 文档、命令参考 |
| 过期内容 | archive/ | 不再维护的资料 |

## Related Projects

- [llm_wiki](https://github.com/nashsu/llm_wiki) — 基于 Karpathy LLM Wiki 概念的桌面应用
- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — 原始设计模式
