# Hermes 接入 Wiki 写入规则

> 归档时间：2026-05-29 08:00 CST  
> 来源会话：`20260528_220341_347550`  
> 类型：笔记备忘

## 今日完成的配置

用户要求 Hermes 在“觉得需要的时候”也能调用 Claude 或自己写入 Wiki。

已完成两层接入：

1. **持久记忆**：记录了 Hermes 可在重要成果出现时主动建议或执行 Wiki 写入。
2. **技能层面**：创建了 `wiki-operations` 技能。

技能路径：

```text
~/.hermes/skills/wiki-operations/SKILL.md
```

## 后续触发条件

遇到以下内容时，Hermes 应优先考虑写入 Wiki，或至少建议用户写入：

- 解决了值得记住的 bug
- 做了关键决策或架构变更
- 分析/借鉴了开源项目设计
- 完成技术调研
- 形成可复用脚本、命令、排障步骤或工作流

## 写入流程

```text
写 .md 页面 → 补交叉引用 → 更新 index.md → append log.md
```

优先方案：让 Claude 按 Wiki 的 `CLAUDE.md` 规则写入。  
备用方案：Claude 不可用时，Hermes 自己按同一 schema 操作 Markdown 文件。

## 注意

Wiki 适合长期知识沉淀，不适合保存临时任务状态、一次性会话摘要、短期进度、会快速过期的编号或提交 SHA。
