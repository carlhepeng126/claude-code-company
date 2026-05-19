# Wiki Schema

## Domain
企业国际化培训 + AI工具与工作流。

涵盖三大核心方向：
1. **企业外语培训** — 商务英语、**涉外业务场景外语沟通**（接待/谈判/邮件/会议/演讲）、小语种（泰语/越南语/西班牙语/阿拉伯语等）、行业英语、语言测评与能力模型
2. **跨文化沟通** — 跨文化沟通（通用场景/商务谈判/团队管理）、跨文化领导力、全球领导力、虚拟团队管理、文化智力（CQ）提升、外派经理赋能
3. **属地化培训** — 本地用工合规、海外团队融入、本地化品牌与运营、东道国政策与商业环境
4. 方法论基座：跨文化培训方法论（R.I.S.E.体系）、客户案例与行业洞察、AI工具最佳实践、项目管理SOP、知识管理架构。

---

## 📂 目录结构

| 目录 | 用途 | 说明 |
|------|------|------|
| `raw/` | 原始素材 | 公众号文章、研究报告、国别文化、培训案例、专项萃取、学习书籍、工具类、行业情报、团队学习资产（assets/）等原始资料 |
| `entities/` | 结构化知识实体 | 人物、工具、案例、竞品、训练产品、书籍萃取、报告、区域、索引 |
| `concepts/` | 提炼后的概念与框架 | 从 raw 和 entities 中提取的通用方法论和概念 |
| `reports/` | 综合报告 | 跨主题的综合性分析报告 |
| `comparisons/` | 对比分析 | 跨区域/跨企业/跨方法论的结构化对比 |
| `方法工具箱/` | 方法论与工具模板 | 咨询参考（麦肯锡/安永等）、课程萃取项目、AI业务专家Agent |
| `索引/` | 主题索引 | 月度专题等索引文件 |
| `诊断报告/` | 客户诊断输出 | 质量评分、客户分析报告 |
| `_archive/` | 归档 | 已过时或被替代的内容，移出索引但保留引用 |

---

# 🧠 知识库运行机制 (Runbook)

Wiki 有四层操作，每层对应一种工作行为：

## 1. Ingest — 摄入

**触发条件：** 有新资料（文章、报告、网页、笔记）到达
**目标：** 提取价值 → 更新/创建 Wiki 页面 → 维护内部链接

### 流程
1. 读取新资料全文
2. 扫描现有 entities/ 和 concepts/，判断是否已有相关内容
3. **有对应页面 → 更新现有页面**（追加新案例、数据）
4. **无对应页面 → 创建新实体卡片或指导框架**
5. 更新 index.md 和 log.md
6. 维护内部链接：在新页面中引用相关现有页面，在相关现有页面中添加反向链接

### 判断规则
- 同一企业/案例有新信息 → 更新 entities/ 中对应卡片
- 某一方向有充足企业案例（3+个）且现有页面未覆盖 → 创建新卡片
- 新方法论/框架 → 更新或创建 concepts/ 中对应条目
- 临时信息/无法归类的 → 放 raw/，不做卡片

---

## 2. Query — 查询

**触发条件：** 用户提出需要跨多个 Wiki 页面综合回答的问题
**目标：** 跨页面检索 → 综合回答（带引用）→ 矛盾标注

### 流程
1. **定位相关页面** — 搜索 entities/ + concepts/ + 必要时 raw/ 中的所有相关文件
2. **提取关键信息** — 从每个页面提取与问题直接相关的段落
3. **综合回答** — 用以下格式输出：

   ```
   ## 问题：<用户问题>

   ### 核心回答
   <综合提炼后的结论>

   ### 引用来源
   - [页面名](entities/xxx.md) § 第X段 — 核心论据摘要
   - [页面名](concepts/xxx.md) § 第Y段 — 补充论据摘要
   - [原始资料](raw/articles/xxx.md) — 原始数据

   ### ⚠️ 矛盾标注（如有）
   - **矛盾点：** 页面 A 说 XX，页面 B 说 YY
     - 页面 A 来源：2025年Q1报告 | 页面 B 来源：2026年市场更新
     - **建议：** 采用页面 B（更新版本）
   ```

4. **如果回答涉及3个以上页面的综合，标记 Query 页面类型**：
   ```
   type: query
   tags: [查询存档, <主题>]
   ```

### 引用格式规范
- 实体/概念页面：`§ 段落关键词`（定位到具体内容区段）
- 原始材料：`§ 原始行号`（如 raw/articles 没有Markdown标题则用行号）

---

## 3. Archive — 归档

**触发条件：** Query 产生了有价值的综合结论
**目标：** 有价值的查询结论存回知识库 → 越用越丰富

### 流程
1. 有价值的查询结论 → 以 `type: query` 页面存入 `queries/` 目录
2. 格式：
   ```yaml
   ---
   title: <查询主题>
   created: YYYY-MM-DD
   type: query
   tags: [查询存档, <主题标签>]
   sources: [entities/xxx.md, concepts/yyy.md, raw/articles/zzz.md]
   confidence: high | medium | low
   ---
   ```
3. 在相关实体/概念页面的 frontmatter 中追加 `related_queries: [query-name]`
4. 更新 index.md（在「查询存档」板块）、log.md
5. 定期回访已归档的 query 页面：当有新素材入库时，检查是否需要更新结论

### 什么值得归档
- 跨 3+ 页面综合的复杂问题回答
- 对 Carl 团队有复用价值的决策参考
- 发现矛盾并给出解决建议的分析
- 涉及多个企业/行业对比的综合分析

---

## 4. Lint — 健康度审计

**触发条件：** 每次 Ingest 完成后，或定期（每月）
**目标：** 检查过时内容、孤立页面、应建未建的连接

### 检查项

| # | 检查项 | 判断标准 | 修复方式 |
|---|--------|---------|---------|
| 1 | **孤立页面** | entities/ 或 concepts/ 中有页面未被任何其他页面引用 | 添加反向链接至相关页面，或将其标记为孤立 |
| 2 | **应建未建** | 3+ 个不同页面都提到了同一实体/概念但尚无对应页面 | 创建新页面并连接 |
| 3 | **过时内容** | 页面中的日期/数据/结论已被新版本 superseded | 更新或标记 `outdated: true` |
| 4 | **悬空链接** | `[[wikilink]]` 指向不存在的文件名 | 创建或修复链接 |
| 5 | **index不同步** | index.md 中列出的文件不存在，或未列出的文件存在 | 更新 index.md |
| 6 | **缺失frontmatter** | entity/concept 页面缺少 YAML frontmatter | 补充标准 frontmatter |
| 7 | **矛盾未标记** | 两页面存在矛盾但未标注 `contested: true` | 更新 frontmatter |

### 输出格式
```markdown
# Lint Report — YYYY-MM-DD

## 🔴 高优先级
- <问题> — <具体文件> — <修复建议>

## 🟡 中优先级
- <问题> — <具体文件>

## ⚪ 低优先级
- <问题>

## ✅ 通过项
- 孤立页面检查：无
- index同步检查：OK
```

### 建议频率
- 每次 Ingest 后：快速 lint（仅 1/3/4/5）
- 每月或每 10 次新素材后：全量 lint（1-7 全部）

---

## Conventions — LLM Wiki 内部
- File names: 中英文均可，优先使用能直观表达内容的中文名（如 `公众号/`、`国别文化/`）；跨文化通用内容可使用英文 lowercase-hyphens
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source.
- **🧠 DEFAULT WORKFLOW: all output → wiki first.** Every substantive piece of work generated
  for Carl (reports, analysis, plans, summaries, cases) MUST be ingested into the wiki as part
  of delivery — either as a new page or as an update to an existing page. The wiki is the
  single source of truth; nothing is "done" until it's in the wiki and the index/log are updated.
  Exceptions: one-shot replies, quick confirmations, throwaway data.

## 🔗 ACT ↔ LLM Wiki 互通规则

两个体系共存于同一个 Obsidian 仓库中，通过 [[wikilinks]] 和字段双向引用：

### 方向 1：ACT 项目 → LLM Wiki（项目启动时）
ACT 项目卡片必须包含 `📎 知识库关联` 区块，列出该项目可调用的现有 wiki 素材：
```
## 📎 知识库关联
- [[LLM Wiki知识应用/entities/xxx.md]]
- [[LLM Wiki知识应用/raw/articles/xxx/xxx.md]]
```
这是**固定区块**，不要求全列，但至少关联 2-3 篇最有价值的素材。

### 方向 2：LLM Wiki → ACT 项目（知识资产反向标注）
entities/concepts 页面可在 frontmatter 中添加 `related_projects` 字段，标注哪些项目用到了该知识：
```yaml
---
type: entity
related_projects: [跨文化谈判课程]
---
```
此字段非必填，萃取时发现关联则加上。

### 方向 3：项目交付 → 知识沉淀（项目完成后）
项目完成/归档时，从 ACT 萃出一条 **entity** 存入 LLM Wiki，格式：
```yaml
---
title: <客户名>-<项目类型>-实战案例
type: entity
source: project
project: <项目名>
created: YYYY-MM-DD
tags: [type/case-study, <行业>, <培训类型>]
---
```
内容包含：客户背景 → 需求分析 → 方案设计 → 交付效果 → 可复用方法论。
萃取的 entity 进入 entities/ 根目录，按 `cases-<项目类型>.md` 命名。

### 互通效果图
```
ACT 笔记                          LLM Wiki 知识应用
──────────                        ─────────────────
3-1-Focus/                      raw/ 原始素材
  ├── 项目卡片 ──[[wikilink]]──→  ├── articles/xxx
  │    │  📎知识库关联             entities/ 应用卡片
  │    │                          ├── cases-xxx ←── 项目沉淀
  │    └── month→月度计划          │    related_projects
  5-Time/ 时间线                  concepts/ 方法论
```

### 维护提醒
- 萃取时（知识虾）：发现素材与某个项目相关 → 更新 entities/concepts 的 related_projects 字段
- 项目复盘时（交付虾）：完成交付 → 萃 entity → 更新 ACT 项目卡片"归档"说明
- 定期检查：entities 中 `related_projects` 指向的项目卡片是否存在（避免悬空引用）

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
---
```

### raw/ Frontmatter
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the body>
---
```

## Tag Taxonomy
- **Training**: methodology, curriculum, assessment, facilitation, cross-cultural, language-training
- **Business**: enterprise-client, industry-insight, case-study, competitive-analysis
- **AI**: llm, tool-comparison, workflow-pipeline, prompt-engineering, agent
- **Project**: delivery, sop, client-management, knowledge-management
- **Meta**: wiki-meta, template, archive

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report