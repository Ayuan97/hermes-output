# GitLab 日报脚本开发记录

> 2026-06-01 · Claude Code 写 → Codex 审 → 人工修 → 最终优化

---

## 背景

需要一个 Python 脚本自动生成公司 GitLab 日报，替代 cron prompt 版本（prompt 版输出质量不可控，容易产生空话）。

---

## 开发流程

| 步骤 | 执行者 | 结果 |
|------|--------|------|
| 1. 写初版 | Claude Code | 134 行，2 个主要缺陷 |
| 2. 审核 | Codex | 发现 14 个问题（5 P0 + 5 P1 + 4 P2） |
| 3. 修复 P0/P1 | 人工（直接写入审核代码） | 全部 10 项修复 ✓ |
| 4. 复审 | Codex | 10/10 全部 ✓ |
| 5. 关键优化 | 人工（发现 `with_stats=true`） | 干掉 ThreadPoolExecutor，精简 24 行 |
| 6. 实跑验证 | 直接运行 | `[SILENT]`（当天暂无新提交，正常） |

---

## 关键技术决策

### 1. 用 `with_stats=true` 替代逐 commit 拉 stats

**之前（慢）：**
```
api(commits) → 逐个 commit 再调 api(commit stats) → ThreadPoolExecutor 5路并发
```

**之后（快）：**
```
api(commits, with_stats=True) → 一次请求，stats 直接返回
```

GitLab Commits API 的列表端点支持 `with_stats=true` 参数，直接在列表响应里返回 `stats.additions` 和 `stats.deletions`，省掉 N+1 次请求。

### 2. 时间窗口双边界

```python
today_start_utc  # 北京时间 00:00 → UTC
today_end_utc    # 北京时间 24:00 → UTC
# MR 用 merged_at 在 [start, end) 区间过滤
```

### 3. 输出格式

- commit 标题从分号拼接改为 bullet 列表
- 每项目最多 5 条
- 去重 + 截断（72 字符）

---

## 修复的关键问题

| 优先级 | 问题 | 修复 |
|--------|------|------|
| P0 | `all=True` 死参数 | 删除 |
| P0 | 逐 commit 串行拉 stats | 先用 ThreadPoolExecutor，后用 `with_stats=true` |
| P0 | MR 时间比较缺少上界 | 加 `today_end_utc` |
| P0 | 单 commit stats 无错误检查 | 加 `raise_for_status()` |
| P1 | 输出 commit 标题全拼太长 | 改 bullet + 截断 |
| P1 | 未使用 `import sys` | 保留（后续可能用 stderr） |
| P1 | Python 3.6 兼容代码 | 删除（本机 3.9+） |
| P1 | 每次请求新建连接 | `requests.Session()` 复用 |

---

## 最终状态

- **路径**: `/Users/administer/Desktop/go/hermes-output/summaries/gitlab_daily_report.py`
- **行数**: 200 行
- **依赖**: `requests`, `urllib3`
- **运行**: `GITLAB_TOKEN=xxx python3 gitlab_daily_report.py`
- **输出**: 无提交时 `[SILENT]`，有提交时生成 Markdown 日报

---

## 与 cron prompt 版的区别

| 特性 | Python 脚本 | cron prompt |
|------|------------|-------------|
| 确定性 | 高（代码固定） | 低（LLM 每次不同） |
| 性能 | 快（单次 API 调用） | 慢（多轮思考） |
| 空话风险 | 无（代码提取 title） | 有（LLM 可能概括） |
| 维护 | 需要改代码 | 改 prompt 即可 |
