# OpenCLI Browser Bridge 完全指南

> 2026-06-01 从实战中梳理。解决「如何让 Hermes Agent 正确操控浏览器」的问题。

---

## 一句话总结

OpenCLI 有两层：**Site Adapters（143 个网站，一行命令）** 和 **Browser 底层命令（手动管理标签页）**。优先用前者。

---

## 两层控制体系

### Tier 1: Site Adapters（首选）

143 个网站适配器，一行命令搞定，自动管理标签页生命周期：

```bash
# 知乎
opencli zhihu hot                          # 热榜
opencli zhihu answer <url> "回答内容"       # 回答问题
opencli zhihu comment <url> "评论内容"      # 评论
opencli zhihu like <url>                   # 点赞
opencli zhihu search <query>               # 搜索

# 微博
opencli weibo hot                          # 热搜
opencli weibo post "内容"                   # 发微博
opencli weibo comments <id>                # 看评论

# GitHub
opencli github issues <repo>               # Issues 列表
opencli github search <query>              # 搜索仓库

# YouTube
opencli youtube search <query>             # 搜索视频

# 通用选项
opencli <site> <cmd> --window background    # 后台运行
opencli <site> <cmd> --site-session ephemeral  # 用完即弃
opencli <site> <cmd> -f yaml               # 结构化输出
```

### 常用 Site Adapter 分类

| 类别 | 站点 |
|------|------|
| **社交/内容** | zhihu, weibo, douyin, xiaohongshu, bilibili, twitter, reddit, instagram, youtube |
| **开发/技术** | github, gitlab, stackoverflow, npm, pypi, dockerhub |
| **购物** | taobao, jd, amazon, xianyu, 1688 |
| **搜索/知识** | google, baidu, wikipedia, arxiv, pubmed |
| **AI** | chatgpt, claude, deepseek, gemini, grok, qwen |
| **金融** | eastmoney, sinafinance, xueqiu, binance |
| **招聘** | boss, linkedin, 51job, indeed |
| **娱乐** | steam, spotify, douban, imdb |

全部 143 个查看：`opencli list`

---

### Tier 2: Browser 底层命令（备选）

**仅在没有 Site Adapter 的目标网站使用。必须手动管理标签页！**

```bash
# 打开页面
opencli browser work open https://xxx.com

# 查看页面状态（获取可交互元素索引）
opencli browser work state

# 点击元素（按 [N] 索引）
opencli browser work click 12

# 输入文本
opencli browser work type 5 "文本"

# 填充表单字段
opencli browser work fill 5 "内容"

# 提取页面为 Markdown
opencli browser work extract

# 执行 JavaScript
opencli browser work eval 'document.title'

# 截图
opencli browser work screenshot /tmp/s.png

# 滚动
opencli browser work scroll down

# ⚠️ 用完必须关闭！
opencli browser work close
```

**标签页管理：**
```bash
opencli browser work tab list            # 列出所有标签页
opencli browser work tab new <url>       # 新建标签页
opencli browser work tab close <id>      # 关闭指定标签页
opencli browser work unbind              # 解绑但不关闭用户的标签页
```

---

## 关键陷阱

1. **用完必须 close** — 不关会积累标签页，用户浏览器越来越乱
2. **优先用 Site Adapter** — 更快、更可靠、自动管理生命周期
3. **不要混淆 OpenCLI / OpenCUA / OpenCode** — 三个不同项目
4. **Browser 命令的 `<session>` 是必填位置参数** — 如 `work`、`research` 等

---

## 查看帮助

```bash
opencli list                                # 所有可用命令
opencli <site> --help -f yaml               # 某站点的所有命令
opencli browser --help                      # Browser 子命令列表
opencli browser work <subcmd> --help        # 子命令详情
```

---

## 相关工具

- **OpenCLI** (`opencli`): 浏览器/网站 CLI 桥梁（本文主角）
- **OpenCUA**: 计算机使用代理研究框架
- **OpenCode** (`opencode`): 编码代理 CLI
