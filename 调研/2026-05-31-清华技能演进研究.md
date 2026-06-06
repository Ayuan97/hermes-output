# 清华 AI Agent 技能演化/优化论文调研

> 归档时间：2026-05-31
> 来源会话：`20260531_070030_fcf7e205`
> 类型：调研报告

## 背景

主子问「清华大学发了两个关于技能的论文，也是技能更新优化的」，并提到一个叫 **Skillvolver** 的关键词。

## 搜索范围

- arXiv API（多轮精准搜索）
- Semantic Scholar（限流后切 arXiv）
- Google Scholar（HTML 解析）
- 清华作者定向搜索（Yujia Qin、Xiao Liu 等）
- 关键词组合：skill library、skill evolution、skill update、agent skill

## 已确认的清华相关论文

### EmbodiSkill — 清华 AIR 参与 ✅

| 属性 | 内容 |
|------|------|
| **标题** | EmbodiSkill |
| **arXiv** | `2605.10332` (2026-05-11) |
| **机构** | 南京大学、华中科技、中科大、**微软研究院**、**清华大学智能产业研究院 (AIR)** |
| **核心** | 具身 agent 的技能自我演化。通过「技能感知反思」区分「技能本身有问题」还是「执行失误」，针对性修正 |
| **成果** | Qwen3.5-27B 冻结执行器达到 93.28% 成功率 |
| **链接** | https://arxiv.org/abs/2605.10332 |

### SkillClaw: Let Skills Evolve Collectively — 待确认清华关联

| 属性 | 内容 |
|------|------|
| **arXiv** | `2604.08377` |
| **主题** | 技能集体演化 |

### You Live More Than Once: Hierarchical Skill Meta-Evolving — 黄民烈组

| 属性 | 内容 |
|------|------|
| **arXiv** | `2605.28390` |
| **清华关联** | **黄民烈（CoAI 组）** |
| **核心** | 技能元演化——「你不止活一次」，层次化技能元演化框架 |

### SkillsInjector: Dynamic Skill Context Construction for LLM Agents

| 属性 | 内容 |
|------|------|
| **arXiv** | `2605.29794` (2026-05-28) |
| **核心** | 动态技能上下文构建。论证「注入更多技能不一定提升效果，甚至可能劣化」 |
| **方法** | 摒弃静态技能注入方式，根据任务动态组织技能上下文 |
| **链接** | https://arxiv.org/abs/2605.29794 |

### SkillBrew: Multi-Objective Curation of Skill Banks for LLM Agents

| 属性 | 内容 |
|------|------|
| **arXiv** | `2605.29440` (2026-05-28) |
| **核心** | 技能库多目标策展。不再「只增不减」，而是删除冗余、过时、有害的技能 |
| **方法** | 多目标优化策展技能库，保持精简有效 |
| **链接** | https://arxiv.org/abs/2605.29440 |

### GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents

| 属性 | 内容 |
|------|------|
| **arXiv** | `2605.29668` (2026-05-28) |
| **核心** | 门控回归感知的技能提议器。自改进过程中确保新技能不退化旧技能 |
| **方法** | 每次添加新 guidance 时检查是否 regression，门控决定是否加入 |
| **链接** | https://arxiv.org/abs/2605.29668 |

## 关于「Skillvolver」

全网（arXiv、Semantic Scholar、GitHub、Google Scholar、OpenReview）均未搜到确切叫 **Skillvolver** 的论文。
最可能的候选是 **You Live More Than Once: Hierarchical Skill Meta-Evolving**（清华黄民烈组），
因为标题中的「Meta-Evolving」和技能演化主题非常贴近。

## 与 Hermes 技能系统的关联

主子关注这个方向，是因为奴才已经在用类似思路维护技能（每次用到技能时现场验证、patch 更新）。
这些论文从学术层面验证了相同方向的可行性：

| Hermes 做法 | 对应论文概念 |
|------------|-------------|
| 用到技能时现场验证 | EmbodiSkill「技能感知反思」 |
| patch 更新过时步骤 | SkillBrew「删冗余更新库」 |
| 修正后保证不破坏旧功能 | GRASP「门控防 regression」 |
| 根据任务调配合适技能 | SkillsInjector「动态上下文构建」 |

## 待确认

- SkillClaw 是否有清华作者参与
- 主子提到的 Skillvolver 是否来自某篇中文公众号/知乎对其主题词的翻译
