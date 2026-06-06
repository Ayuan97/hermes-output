# Hermes 调用 Claude / Codex 作为子代理的常见用法（2026-05-28）

## 核心结论

社区主流不是让一个智能体从头干到尾，而是：

> 主代理负责拆任务、控冲突、验收结果；Claude / Codex 子代理负责具体执行。

一句话分工：

- **Claude：想、审、验**
- **Codex：改、测、提交**
- **Hermes 主代理：拆任务、调度、控冲突、最终汇总**

## 两种调用方式

### 方式一：把 Claude / Codex 当 Hermes 主模型

适合日常聊天、Telegram 入口、自动化、定时任务、工具调用和技能加载。

常见命令：

```bash
hermes model
```

Claude 常见配置：

```bash
hermes config set model.provider anthropic
hermes config set model.default claude-sonnet-4-5
```

Codex / GPT 系列常见配置：

```bash
hermes auth add openai-codex
hermes config set model.provider openai-codex
hermes config set model.default gpt-5.1-codex
```

临时指定模型示例：

```bash
hermes chat --provider anthropic -m claude-sonnet-4-5 -q "分析这个问题"
hermes chat --provider openai-codex -m gpt-5.1-codex -q "写一个实现方案"
```

### 方式二：Hermes 作为调度器，启动本机 Claude Code / Codex CLI

适合真实代码仓库开发、大改动、跑测试、提交 PR、并行代理工作。

Claude Code 示例：

```bash
claude -p "阅读当前仓库，找出登录失败原因并修复" --max-turns 10
```

主子本机常用快捷命令：

```bash
cl "修复这个 bug，并运行测试"
```

Codex CLI 示例：

```bash
codex exec --full-auto "修复 failing tests，并提交修改"
```

## 社区常见模式

### 1. 主代理当调度员

流程：

1. 主代理理解需求。
2. 拆成多个可独立完成的小任务。
3. 判断哪些任务会改同一批文件。
4. 不冲突的任务并行交给多个子代理。
5. 冲突任务排队执行。
6. 子代理返回结果、补丁、测试结果或提交。
7. 主代理统一审查、跑测试、合并结论。

### 2. Claude 更适合复杂推理和审查

适合交给 Claude 的任务：

- 需求分析
- 架构设计
- 多文件理解
- 重构方案
- 代码审查
- 安全审查
- 最终验收

示例：

```bash
claude -p "审查这个实现是否满足需求，并指出风险" --max-turns 5
```

### 3. Codex 更适合明确执行

适合交给 Codex 的任务：

- 修一个明确 bug
- 改一个模块
- 补测试
- 批量处理简单 issue
- 执行已有计划
- 生成提交

示例：

```bash
codex exec --full-auto "根据计划实现 auth 模块的错误处理，并补充测试"
```

### 4. 多 Codex 并行要用隔离工作区

并行时不要让多个子代理同时改同一批文件。推荐用 `git worktree` 隔离：

```bash
git worktree add /tmp/task-a -b task-a main
git worktree add /tmp/task-b -b task-b main
```

每个 Codex 在自己的目录中执行：

```bash
cd /tmp/task-a && codex exec --full-auto "完成任务 A"
cd /tmp/task-b && codex exec --full-auto "完成任务 B"
```

主代理最后再审查差异、跑测试、合并。

### 5. Claude 调 Codex 的桥接模式

社区里也常见这种桥接：

1. Claude 理解用户需求；
2. Claude 把需求改写成适合 Codex 执行的提示词；
3. 只调用一次 Codex；
4. Claude 不和 Codex 抢着改代码，只做结果解释或审查。

适合把复杂自然语言需求外包成明确工程任务。

## 推荐给主子的实际用法

### 小任务

直接用 Codex：

```bash
codex exec --full-auto "完成这个明确修改，并运行相关测试"
```

### 复杂任务

用 Claude 做规划和审查，Codex 做执行：

1. Claude 分析需求和拆任务；
2. Hermes 判断冲突和执行顺序；
3. Codex 分任务实现；
4. Claude 审查实现；
5. Hermes 跑测试、汇总结果。

### 本机长期分工

- **Hermes 主模型**：负责 Telegram 入口、自动化、定时任务、工具调用、记忆和技能。
- **Claude Code / `cl`**：复杂编码、仓库理解、审查、重构规划。
- **Codex CLI**：明确代码修改、补测试、批量修复、提交。
- **Hermes `delegate_task`**：适合拆分研究、分析、审查，但不完全等同于外部 Claude Code / Codex CLI。

## 避坑

- 不要让多个子代理同时改同一批文件。
- 不要把模糊大任务直接丢给 Codex；先拆小。
- 不要让 Claude 和 Codex 同时充当“主控”，否则容易重复劳动。
- 子代理输出要可验证：补丁、测试结果、提交或文件路径。
- 主代理必须做最终验收，不能直接相信子代理自报成功。
