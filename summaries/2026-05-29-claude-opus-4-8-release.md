# Claude Opus 4.8 发布调研摘要

> 归档时间：2026-05-29 08:00 CST  
> 来源会话：`20260529_053245_9501abb4`  
> 类型：调研报告

## 核心结论

这次不是 “Claude App 4.8”，而是 **Claude Opus 4.8** 模型发布。

发布时间：**2026-05-28**  
模型 ID：

```text
claude-opus-4-8
```

Claude Opus 4.8 是 Opus 4.7 的增强版，重点强化：

- 长时间编码任务
- 大型代码库迁移
- 多工具调用
- 自主代理任务
- 长上下文任务
- Claude Code 里的复杂工程活

官方定位：Anthropic 当前最强的通用可用模型。

## 主要更新

### 1. 编码和代理能力更强

相比 Opus 4.7，官方强调：

- 长程 agentic coding 更稳
- 长上下文处理更好
- 更少触发上下文压缩
- 压缩后恢复任务状态更稳
- 工具调用更准，减少“该调工具却跳过”的情况
- 更适合跑长时间异步任务和多步骤工程改造

### 2. Claude Code 新增 Dynamic workflows

Claude Code 新增研究预览功能：`Dynamic workflows`。

能力描述：

- 先规划任务
- 在一个会话里运行数百个并行 subagents
- 自己验证结果
- 最后汇总给用户

典型用途：

- 大型代码库迁移
- 几十万行代码级别的改造
- 多模块并行修复
- 从任务启动、测试到合并前检查的一条龙流程

限制：

- 研究预览阶段
- 面向 Claude Code Enterprise / Team / Max 计划

### 3. claude.ai / Cowork 增加 Effort 控制

网页端和相关工作流增加类似“投入程度”的控制：

- 低 effort：更快，省额度
- 高 effort：思考更多，质量更好
- extra / max：适合困难任务、长任务、异步工作流

Opus 4.8 默认是 `high effort`。困难任务建议使用更高 effort。

### 4. API 支持中途插入 system message

Messages API 支持在对话中间插入系统消息：

```json
{
  "role": "system",
  "content": "新的系统指令"
}
```

用途：

- 长任务中途更新权限
- 更新环境信息
- 调整 token 预算
- 修改 agent 执行约束
- 不必重新塞完整 system prompt

好处：

- 不破坏 prompt cache
- 降低长任务成本
- 更适合 agent 循环

### 5. 默认 1M 上下文，最大输出 128k

官方规格：

- Claude API：1M tokens 上下文
- AWS Bedrock：1M tokens
- Google Vertex AI：1M tokens
- Microsoft Foundry：200k tokens
- 最大输出：128k tokens

适合大代码库、长日志、长文档和复杂项目分析。

### 6. Fast mode 更快，价格比前代便宜

Opus 4.8 支持 API 的 Fast mode 研究预览。

特点：

- 设置 `speed: "fast"`
- 输出速度最高 2.5 倍
- 是同一个模型，不是降智版
- 主要提升输出 token 速度，不一定明显缩短首 token 时间

普通 Opus 4.8 价格：

```text
输入：$5 / MTok
输出：$25 / MTok
```

Fast mode Opus 4.8 价格：

```text
输入：$10 / MTok
输出：$50 / MTok
```

对比 Opus 4.6 / 4.7 的 Fast mode：

```text
旧 Fast mode：$30 / $150
Opus 4.8 Fast mode：$10 / $50
```

所以官方称 Fast mode 价格比前代便宜约 3 倍。

限制：

- 目前只在 Claude API 研究预览
- 不支持 Bedrock / Vertex / Microsoft Foundry
- 需要 account manager 或 waitlist

### 7. Prompt cache 门槛降到 1024 tokens

Opus 4.8 的可缓存 prompt 最小长度降低到：

```text
1024 tokens
```

这对 agent 循环、多轮代码任务和成本控制有帮助。

### 8. 更诚实，少“硬装完成”

官方强调 Opus 4.8 的 honesty 更好：

- 不确定时更愿意标出来
- 不太会没干完硬说干完
- 写代码后更可能主动指出自己代码里的问题
- 更少无依据断言

对自动编码很关键，因为它减少了“错了但很自信”的风险。

## API 注意事项

### 模型 ID

```text
claude-opus-4-8
```

### 不支持传统采样参数的非默认值

以下参数设为非默认值可能报 400：

```text
temperature
top_p
top_k
```

### 不支持旧的 extended thinking budget 写法

旧写法：

```json
{
  "thinking": {
    "type": "enabled",
    "budget_tokens": 32000
  }
}
```

推荐写法：

```json
{
  "thinking": {
    "type": "adaptive"
  },
  "output_config": {
    "effort": "high"
  }
}
```

### 默认 effort 是 high

如果想省钱、省额度，需要显式调低。

## 对本地工作流的价值

最值得关注的点：

1. Claude Code 能力增强，更适合大型工程改造和本地 `cl` 长任务。
2. Dynamic workflows 适合超大任务并行代理。
3. 工具调用更准，对 Claude Code、Hermes 和 agent 自动化都重要。
4. 更诚实，适合做代码验收前置。
5. 1M 上下文 + 128k 输出，适合大仓库、长日志、公司报告和技术文档分析。

## 官方来源

- [Anthropic 新闻：Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)
- [Claude API 文档：What's new in Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8)
- [Claude Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Fast mode 文档](https://platform.claude.com/docs/en/build-with-claude/fast-mode)

一句话：**Claude Opus 4.8 不是革命性换代，但对 Claude Code、长任务、agent 编码和工具调用来说，是一次很实用的增强。**
