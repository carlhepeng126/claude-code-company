# ACT 笔记 · 入口

> **行动 · 卡片 · 时间**

### ACT 系统 · 一张图

```
📥 1-收件箱（临时暂存，待分类）
    │
    ├── 🎯 Action（3-Action/） → 我要做什么
    │   ├── 3-1-Focus/        当前聚焦项目
    │   ├── 3-2-Active/       正在跟进
    │   └── 3-3-Maybe/        将来也许
    │
    ├── 🧠 Card（4-Card/）     → 我知道什么
    │   ├── 4-1-IndexCard/    主题索引
    │   ├── 4-2-BibCard/      阅读笔记
    │   └── 4-3-MainCard/     核心知识
    │
    ├── 📅 Time（5-Time/）     → 我什么时候做
    │   ├── 5-1-Vision/       长期愿景
    │   ├── 5-2-Monthly/      月度计划
    │   ├── 5-3-Weekly/       周计划
    │   └── 5-4-Daily/        日日志
    │
    └── 🗄️ Storage（6-storage/）→ 我存了什么
        ├── 6-1-archive/      归档
        ├── 6-2-template/     模板
        ├── 6-3-picture/      图片
        └── 6-4-base/         数据视图
```

### 每日工作流

```
📥 1-收件箱 → 快速捕捉 → 分类 → 行动/知识/时间 → 归档
         ↑                          ↓
         └──── 每周回顾清空 ────────┘
```

### 不用动脑 · 判断指南

遇到一个想法 → **先丢进1-收件箱**

| 回顾时问自己 | → 放哪里 | 用什么模板 |
|-------------|---------|-----------|
| **要马上去做？** | 3-1-Focus/ 或 3-2-Active/ | 行动卡片模板 |
| **以后可能想做？** | 3-3-Maybe/ | 将来也许模板 |
| **想记住这个知识？** | 4-3-MainCard/ | 核心卡模板 |
| **读书/文章有感？** | 4-2-BibCard/ | 阅读卡模板 |
| **今天做了啥？** | 5-4-Daily/ | 日计划模板 |
| **只是随便记一下？** | 1-收件箱/ | 随心记模板 |

> 💡 **记不住先别想** → 全部丢收件箱。每周回顾再分。
> 模板记不住也没关系 → 打开时直接写，空字段可以跳过。

### 项目生命周期

```
Maybe(3-3) → Active(3-2) → Focus(3-1) → 完成归档到 6-1-archive/项目归档/
```

## 🔗 与 LLM Wiki 的关系

> ACT 做「我在做什么」，LLM Wiki 做「我知道什么」。

```mermaid
flowchart LR
    A[🎯 ACT笔记] -->|📎知识库关联| B[🧠 LLM Wiki知识库]
    B -->|项目启动引用素材| A
    A -->|项目完成→萃entity| B
```

**分工：**
| 体系 | 管什么 | 放哪里 |
|------|--------|--------|
| 🎯 **ACT 笔记** | 你要做的项目、时间线、日周月计划、个人成长 | `~/wiki/ACT笔记-深度思考/` |
| 🧠 **LLM Wiki** | 专业知识素材、案例库、方法论框架 | `~/wiki/LLM Wiki知识应用/` |

**怎么互通：**
- 新项目启动 → 在项目卡片「📎 知识库关联」区块引用 LLM Wiki 素材
- 素材摄入时发现与项目相关 → 在 entity frontmatter 加 `related_projects`
- 项目交付完成 → 萃实战案例成 entity 存回 LLM Wiki

> 💡 在 Obsidian 中，`[[wikilink]]` 可以跨目录直接引用，例如
> `[[LLM Wiki知识应用/entities/cases-negotiation.md]]`

---

## 📋 快速索引

```dataview
TABLE WITHOUT ID
  rows.file.name as "笔记"
FROM "ACT笔记-深度思考"
WHERE file.name != "README.md"
  AND !contains(file.path, "6-2-template-模板")
  AND !contains(file.path, "6-4-base-数据视图")
  AND !contains(file.path, "6-3-picture-照片")
  AND !contains(file.path, "1-收件箱")
  AND file.ext = "md"
SORT file.folder ASC, file.name ASC
GROUP BY file.folder AS "文件夹"
```