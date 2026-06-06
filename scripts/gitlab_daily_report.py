#!/usr/bin/env python3
"""GitLab 当天 commit/MR 中文日报生成器。

调用 GitLab API 拉取北京时间当天活跃项目的 commits 与 MR，
统计 additions/deletions，按提交排行输出中文日报。

无提交 → 输出 [SILENT]，不写文件。周日 → 输出 [SILENT]，不写文件。
"""
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE = "https://gitlab.e-idear.com"
TOKEN = os.environ.get("GITLAB_TOKEN")
if not TOKEN:
    print("错误: 请设置 GITLAB_TOKEN 环境变量", file=sys.stderr)
    sys.exit(1)

HEADERS = {"PRIVATE-TOKEN": TOKEN}
BJ = timezone(timedelta(hours=8))
MAX_TITLES = 8  # 每个项目最多展示 8 条 commit

# 复用 TCP 连接
session = requests.Session()
session.headers.update(HEADERS)
session.verify = False


def api(path: str, **params: Any) -> list[dict[str, Any]]:
    """分页拉取 GitLab API，返回聚合后的全部条目。"""
    out: list[dict[str, Any]] = []
    params.setdefault("per_page", 100)
    page = 1
    while True:
        params["page"] = page
        r = session.get(f"{BASE}/api/v4{path}", params=params, timeout=30)
        r.raise_for_status()
        data: list[dict[str, Any]] = r.json()
        if not data:
            break
        out.extend(data)
        if len(data) < params["per_page"]:
            break
        page += 1
    return out


def main() -> None:
    now = datetime.now(BJ)

    # 周日静默
    if now.weekday() == 6:
        print("[SILENT]")
        return

    # 今天北京时间 00:00 - 24:00，转 UTC 传给 GitLab API
    today_start_bj = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end_bj = today_start_bj + timedelta(days=1)
    today_start_utc = today_start_bj.astimezone(timezone.utc)
    today_end_utc = today_end_bj.astimezone(timezone.utc)
    since = today_start_utc.isoformat()
    date_str = now.strftime("%Y-%m-%d")

    # 拉全部成员项目（不用 last_activity_after 防漏报）
    projects = api(
        "/projects",
        membership=True,
        simple=False,
        order_by="last_activity_at",
        sort="desc",
    )

    proj_commits: dict[str, list[str]] = {}
    author_stats: dict[str, dict[str, int]] = defaultdict(
        lambda: {"count": 0, "adds": 0, "dels": 0}
    )
    merged_mrs: list[tuple[str, int, str, str]] = []

    for p in projects:
        pid: int = p["id"]
        name: str = p["path_with_namespace"]

        # 拉当天 commits（GitLab API 支持 with_stats=true 直接返回 stats）
        commits = api(
            f"/projects/{pid}/repository/commits",
            since=since,
            with_stats=True,
        )
        if not commits:
            # 也拉 MR（即使无 commit）
            mrs = api(
                f"/projects/{pid}/merge_requests",
                state="merged",
                updated_after=since,
            )
            for m in mrs:
                merged_at = m.get("merged_at")
                if not merged_at:
                    continue
                merged_dt = datetime.fromisoformat(merged_at.replace("Z", "+00:00"))
                if today_start_utc <= merged_dt < today_end_utc:
                    merged_mrs.append(
                        (
                            name,
                            m["iid"],
                            m["title"],
                            (m.get("author") or {}).get("name", "?"),
                        )
                    )
            continue

        titles: list[str] = []
        for c in commits:
            titles.append(c["title"])
            author = c.get("author_name") or c.get("committer_name") or "unknown"
            author_stats[author]["count"] += 1
            st = c.get("stats") or {}
            author_stats[author]["adds"] += st.get("additions", 0)
            author_stats[author]["dels"] += st.get("deletions", 0)

        if titles:
            proj_commits[name] = titles

        # 拉今天合入的 MR
        mrs = api(
            f"/projects/{pid}/merge_requests",
            state="merged",
            updated_after=since,
        )
        for m in mrs:
            merged_at = m.get("merged_at")
            if not merged_at:
                continue
            merged_dt = datetime.fromisoformat(merged_at.replace("Z", "+00:00"))
            if today_start_utc <= merged_dt < today_end_utc:
                merged_mrs.append(
                    (
                        name,
                        m["iid"],
                        m["title"],
                        (m.get("author") or {}).get("name", "?"),
                    )
                )

    if not author_stats:
        print("[SILENT]")
        return

    # 构建输出
    lines: list[str] = [f"📅 {date_str} · GitLab 日报", "", "【项目】"]

    for name, titles in sorted(proj_commits.items(), key=lambda kv: -len(kv[1])):
        # 去重 + 去空
        unique_titles = list(
            dict.fromkeys(t.strip() for t in titles if t.strip())
        )
        if not unique_titles:
            continue
        shown = unique_titles[:MAX_TITLES]
        lines.append(f"**{name.split('/')[-1]}**（{len(unique_titles)} 次提交）")
        for t in shown:
            lines.append(f"  • {t}")
        if len(unique_titles) > MAX_TITLES:
            lines.append(f"  • … 还有 {len(unique_titles) - MAX_TITLES} 条")

    lines.append("")
    lines.append("【提交排行】")
    medals = ["🥇", "🥈", "🥉"]
    ranked = sorted(author_stats.items(), key=lambda kv: -kv[1]["count"])
    for i, (author, s) in enumerate(ranked):
        medal = medals[i] if i < len(medals) else "  "
        lines.append(f"{medal} {author}：{s['count']} 次 / +{s['adds']} -{s['dels']}")

    if merged_mrs:
        lines.append("")
        lines.append("【MR 合入】")
        for name, iid, title, author in merged_mrs:
            lines.append(f"{name.split('/')[-1]}!{iid}：{title}（{author}）")

    report = "\n".join(lines)
    print(report)

    # 写入文件
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f"{date_str}_gitlab_daily.md",
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report + "\n")


if __name__ == "__main__":
    main()
