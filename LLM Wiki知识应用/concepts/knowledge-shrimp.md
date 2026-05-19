---
title: 知识虾 — 知识库核心大脑
created: 2026-05-10
type: concept
tags: [type/模型, 知识管理]
maturity: sapling
context: [内部运营, 方案设计, 课程交付]
related_concepts: 
---

# 知识虾 🧠 — 知识库核心大脑

> 负责 LLM Wiki 整体建构和维护。从 raw 素材（articles + assets）中萃取有价值的知识，存入 entities（应用卡片）/ concepts（方法论框架），更新 index + log，打通 ACT 笔记与企业知识库的双向引用。

## 知识库结构

```
~/wiki/LLM Wiki知识应用/
├── concepts/         ← 方法论/框架/模型（高频复用）
├── entities/         ← 企业案例/区域数据/应用索引
├── raw/
│   ├── articles/     ← 原始素材
│   ├── assets/       ← 剪藏归集
│   └── 深度学习萃取/ ← 已萃取的批次文件
├── comparisons/      ← 对比分析
├── index.md          ← 总索引
└── log.md            ← 变更日志
```

## 萃取三步法

### 1. 评估
- 新案例 / 新数据 / 新方法论 → 值得萃取
- 已有信息的补充 → 更新现有页面
- 重复内容 → 跳过

### 2. 定位

| 类型 | 去向 | 命名示例 |
|------|------|---------|
| 企业案例 | `entities/cases-*.md` | `cases-negotiation.md` |
| 区域数据 | `entities/region-*.md` | `region-vietnam.md` |
| 方法论 | `concepts/*.md` | `structured-strategic-thinking.md` |
| 对比分析 | `comparisons/*.md` | `tool-comparison.md` |

### 3. 关联
- 新卡片引用 2+ 已有页面（`[[wikilinks]]`）
- 使用 `related_projects` 字段打通 ACT ↔ LLM Wiki
- 反向更新被引用页的 frontmatter

## 情报源摄入

当出海日报/情报虾周报累积到阈值时，知识虾将其提炼为知识资产：

1. **扫描** — `clam-knowledge-ingestion.py` 扫描最近 7 天信号
2. **过滤** — 央国企案例→entities、方法论→concepts、低价值→跳过
3. **创建/更新** — 写入 wiki + 维护 index.md + log.md
4. **关闭循环** — 在信号源文件追加 `[已萃取] → see [[entities/xxx.md]]`

**优先级：** 🔴央国企案例/新基地/竞品产品变化 > 🟡趋势数据/用工变化 > 🟢通用趋势

## 情报系统维护公约

所有情报系统的一级架构文档统一归集在 `concepts/intelligence-collection-pipeline.md`（3层管道 × 4级信号源 × 6路输出 × Cron编排 × 扩展机制 × 质量保障），核心索引在 `~/wiki/信息情报收集链路思路.md`。

> **每次新增/修改信号源、调整爬虫、改动输出格式、添加 cron 任务或变更处理管道后，同步更新上述两个文件。**

## 知识活化三件套

| 机制 | 方式 | 场景 |
|------|------|------|
| 🚀 Push | 工作日 09:00 飞书每日知识卡片 | 被动接收日常刷到 |
| 🔍 Pull | 飞书发「查知识 [关键词]」 | 有明确需求时查询 |
| 🧭 Browse | Dashboard 知识推荐模块 | 无目的闲逛发现关联 |

详见 `skill:knowledge-shrimp`。
