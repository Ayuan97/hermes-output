# 金价监控脚本 SSL 崩溃修复与周末数据过期检测

> 归档时间：2026-05-31
> 来源会话：`20260531_021210_b8754871`
> 类型：教程类 / 排障记录

## 问题背景

金价监控脚本 `gold_price_watch.py`（每 15 分钟跑一次）间歇性崩溃，报 `SSL: UNEXPECTED_EOF_WHILE_READING`，
大约 30% 运行会挂掉。根因：macOS 的 LibreSSL + VPN 环境跟 Stooq 服务器 SSL 握手偶尔失败，`urllib` 直接抛异常退出导致非零 exit code → cron 报错。

## 修复内容（2026-05-29 第一次修复）

在原脚本基础上加了三层防护：

1. **重试机制**：urllib 失败后自动重试 3 次，指数退避（2s → 4s → 8s）
2. **自定义 SSL context**：干净握手，避免 LibreSSL 的兼容性问题
3. **curl 兜底**：urllib 全部失败后，自动切 `curl --http1.1` 抓数据

## 第二次修复（2026-05-31）— 周末数据过期检测

修复后 SSL 崩溃不再发生，但主子发现脚本依然「异常」—— 周末市场休市，Stooq 返回的一直是周五收盘价，
脚本每 15 分钟静默空转，数据不更新，也不会发任何提醒。

### 新增功能

- **报价时间戳检测**：对比 `quote_date` 与当前时间，超过 24 小时未更新则输出警告
- **6 小时冷却**：同一过期提醒每 6 小时最多发一次，不会刷屏
- **连续失败计数**：抓取失败静默记录，超过 3 次连续失败再发提醒
- **curl 也加重试**：curl 兜底加 `--http1.1 --connect-timeout --max-time`
- **金价增加 Yahoo Finance 兜底**：除了 Stooq XAUUSD，增加 Yahoo Finance `GC=F`（黄金期货价）作为金价备用源

### 验证结果

```
第一次跑：输出过期警告 ⚠️
第二次跑（6h 冷却内）：静默无输出
exit 0 ✅
```

## 脚本位置

```text
~/.hermes/scripts/gold_price_watch.py
```

## 状态文件

```text
~/.hermes/state/gold_price_watch.json
```

包含：上次提醒价格、最新报价、阈值、初始化时间、上次提醒时间。

## 后续排障清单

如果再次出现异常：

1. 检查 cron 输出日志：`ls -lt ~/.hermes/cron/output/ | grep -i gold`
2. 检查状态文件：`cat ~/.hermes/state/gold_price_watch.json`
3. 手动运行脚本：`cd ~/.hermes && python3 scripts/gold_price_watch.py`
4. 检查数据源可用性：
   - Stooq XAUUSD: `curl -s "https://stooq.com/q/l/?s=xauusd&f=sd2t2ohlcv&h&e=csv"`
   - Stooq USDCNY: `curl -s "https://stooq.com/q/l/?s=usdcny&f=sd2t2ohlcv&h&e=csv"`
   - Yahoo Finance: `curl -s "https://query1.finance.yahoo.com/v8/finance/chart/GC%3DF?range=1d&interval=1m"`
