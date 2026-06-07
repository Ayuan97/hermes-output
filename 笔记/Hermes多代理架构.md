# Hermes 多 Agent 体系速查

> 2026-06-01 整理。四层架构从轻到重。

---

## 总览

| 层级 | 方式 | 用途 | 生命周期 |
|------|------|------|----------|
| 1 | `delegate_task` | 子代理委派，干完汇报 | 寄生在主会话，打断即灭 |
| 2 | Spawn 独立进程 | 完全独立的 Hermes agent | 长期存活，独立配置 |
| 3 | Kanban 看板 | 多 worker 自动抢活 | 任务队列持续运转 |
| 4 | Cron 定时 | 到点自动触发 | 按 schedule 重复 |

---

## 1. delegate_task — 子代理委派

最常用。把杂活抛出去，不占主会话上下文窗口。

```python
delegate_task(
    goal="审核 gitlab_daily_report.py，找出所有问题",
    context="脚本路径: /path/to/script.py，重点看 API 调用、性能、错误处理",
    toolsets=["terminal", "file"]
)
```

**特点：**
- 子代理有独立终端、独立上下文
- 最多并行 3 个
- 同步执行，结果汇总返回
- 只返回摘要，不污染父会话

**适合：** 查资料、对比方案、审代码、并行多任务

---

## 2. Spawn 独立进程 — 衍生完整 Hermes

通过 tmux 启动全新 Hermes 进程，不同配置、模型、工作目录。

```bash
# 通过 tmux 启动独立 agent
hermes spawn --profile worker-1 --model gpt-5.5
```

**特点：**
- 真正独立，不寄生
- 可跑几小时甚至几天
- 不同 profile 完全隔离

**适合：** 持续监控、长时间爬数据、大规模分析

---

## 3. Kanban 看板系统

多 agent 协作的任务队列。

```
调度器 → 任务池 → worker-1 抢活 A
                 → worker-2 抢活 B
                 → worker-3 抢活 C
```

**适合：** 多项目并行开发、多仓库代码审查

---

## 4. Cron 定时任务

定期触发的自动化 agent。

当前运行的 cron jobs：
- 每日工作总结（08:00）
- 每日 AI 早报（09:00）
- 每周视频选题研究（周一 09:00）
- 公司 GitLab 日报（18:00）
- 金价监控（每 15 分钟）

---

## 多平台接入

Hermes 同一 Gateway 可同时接入多个平台：

- Telegram ✓（已配置）
- 微信（可加，扫码登录）
- Discord
- Slack

**共享 vs 隔离：**

| 方式 | 命令 | 效果 |
|------|------|------|
| 同一 Gateway | `hermes gateway setup` 加平台 | 共享记忆/人格 |
| 不同 Profile | `hermes profile create xxx` | 完全隔离 |

---

## 当前配置

- **默认模型**: `gpt-5.5`（`openai-codex` 提供方）
- **备用模型**: `deepseek-v4-pro`（deepseek）
- **工作目录**: `/Users/administer/.hermes/hermes-agent`
- **输出仓库**: `~/Desktop/go/hermes-output/`
