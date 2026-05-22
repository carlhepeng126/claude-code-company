---
name: course-brochure-builder
description: >
  Use this skill whenever the user asks to extract a course system, training framework, or tool suite from a report/document, or asks to build a promotional brochure, handbook, or manual for a training product. Triggers on phrases like "根据这个报告萃取课程体系", "帮我做成宣传册", "设计工具套件", "生成课程手册", "把这个文档做成培训方案", "出一本手册", "做一个能马上用的XX体系". Also triggers when the user provides a PDF/long document and asks to turn it into actionable training materials. This skill encapsulates the full pipeline: knowledge extraction → course system design → tool template generation → document system architecture → HTML brochure with professional design → rendering.
---

# Course Brochure Builder

从一份行业报告或长文档出发，端到端生成一套"能马上用的课程体系 + 工具套件 + 宣传册"。

## 工作流总览

```
源文档 → [1.萃取] → [2.课程体系] → [3.工具套件] → [4.文档体系] → [5.HTML宣传册] → [6.渲染输出]
```

每一步都有明确的产出物。不要跳过步骤。

---

## 第1步：深度萃取

读取用户提供的源文档（PDF/Word/长文），提取以下内容：

**必须提取的要素**：
- 核心框架：文档的主要章节结构和逻辑主线
- 关键模型：任何框架图、矩阵、金字塔、循环模型
- 数据点：百分比、统计数据、基准数据
- 方法论：可操作的方法、流程、步骤
- 工具/模板线索：任何可以转化成填空模板的内容

**产出格式**：
```
## 萃取摘要
### 报告核心框架（3-5句话概括）
### 可转化为课程的模块（列表，每个标注来源页码）
### 关键数据点（可引用的数据）
### 核心模型清单（名称+一句话描述）
```

---

## 第2步：设计课程体系

基于萃取内容，遵循以下方法论设计课程体系：

**B011 问题解决铁律**：目标→策略→流程→分工，不可跳跃不可颠倒
**B016 五原则**：聚焦专业能力、短板全覆盖、实战密度高、晚间结构化分享、工具输出
**B002 SOP四步法**：找本质→定SOP→轻试行→复盘沉淀

**产出1：课程模块矩阵**

| 模块 | 解决什么HR痛点 | 核心交付 | 工具编号 | 建议时长 |
|------|---------------|---------|---------|---------|
| M1... | ... | ... | 01-04 | 1天 |

**产出2：模块进阶金字塔**
从下到上的递进结构，标注每层的逻辑关系。格式：
- 第一层（基座）：选对人/入口
- 第二层（支柱）：育成材/引擎
- 第三层（护栏）：防住险/防线
- 第四层（塔尖）：策到位/落地
- 横向贯穿：工具箱

**产出3：三天课程结构**
Day 1 / Day 2 / Day 3，每半天标注主题和实战环节。

---

## 第3步：生成工具套件

为每个课程模块设计"填空即用"的工具模板。工具设计遵循以下分类：

**选拔类**：胜任力模型、评鉴方案、访谈指南、决策矩阵
**培养类**：培训方案、导师制手册、复盘模板、知识管理、发展计划
**合规类**：自检清单、手册框架、SOP流程
**策略类**：策略画布、资源清单

**每个工具包含**：
1. 工具编号 + 名称 + 星级（★★★核心/★★重要/★进阶）
2. 一句话说明"什么时候用"
3. 模板正文（结构化表单格式）

参考 `references/tool-patterns.md` 中的表单样式模板。

---

## 第4步：设计文档体系

设计全生命周期文档地图，覆盖全流程：

**A类·战略规划期**（持续）— 人才盘点、路线图、策略书
**B类·选拔期**（T-6→T-4月）— 胜任力、评鉴、家庭评估、决策
**C类·派前集训期**（T-4→出发）— 集训记录、协议、导师确认、IDP
**D类·派驻执行期**（抵达→归前6月）— 安顿、复盘、合规自检、冲突记录
**E类·回流期**（归前6月→归后12月）— 知识资产、交接、回任、总结

每份文档标注：编号、名称、产出时机、负责方、对应工具。

**文档成熟度自评**：Lv.0 无文档 → Lv.1 有选拔 → Lv.2 全周期 → Lv.3 文档驱动

---

## 第5步：构建HTML宣传册/手册

这是核心输出。根据用途选择输出类型：

**如果是宣传册**（14页，用来推广课程）→ 参考 `references/brochure-structure.md`
**如果是完整手册**（30页，用来交付工具）→ 参考 `references/manual-structure.md`

### 设计规范（必须遵守）

**美学方向**：Editorial Architecture — 建筑杂志式的编辑美学。大尺度排版对比、几何精确、金色只做锐利点缀不铺满。

**色板**：
- 主色 `#1B2A4A` 深蓝
- 辅色 `#C8963E` 金色
- 底色 `#FAF8F5` 米白
- 强调 `#2C5282` 藏青

**字体**：
- 标题：Noto Serif SC（思源宋体）
- 正文：Noto Sans SC（思源黑体）
- 英文装饰：Playfair Display
- 禁止使用：Inter、Roboto、Arial、system fonts

**禁止事项**：
- 蓝紫渐变
- 统一的卡片布局模板
- ASCII框线（┌─┐└─┘等）
- 纯色背景（需加噪点纹理）
- cookie-cutter AI美学

**页面节奏**：深色页面（封面/章节页/关于/封底）和浅色页面（内容页）交替出现，形成明暗呼吸节奏。

**工具模板**在HTML中应呈现为：白底卡片 + 圆角 + 淡阴影 + 虚线填空区 + 结构化表单，而非代码块。

**CSS规范**：
```css
@page { size: A4; margin: 0; }
@media print { body { background: white; } .page { page-break-after: always; } }
```

### 噪点纹理（所有浅色页必须使用）
```css
.page::before {
  content: '';
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.02'/%3E%3C/svg%3E");
  opacity: 0.5;
}
```

---

## 第6步：渲染输出

### 多页PDF
提示用户：浏览器打开HTML → Ctrl+P → 另存为PDF。CSS的 @page 和 page-break-after 会自动分页。

### 单页宣传图
使用 dgw-canva 工具：
```bash
dgw-canva render --html "path/to/brochure.html" --preset instagram-story --output "path/to/output" --format png
```

**可用预设**：instagram-post (1080×1080) / instagram-story (1080×1920) / facebook-post (1200×630) / landing-hero (1920×1080)

**注意**：dgw-canva 只能渲染单页（截取viewport大小的画面），适合生成社交媒体宣传图，不适合多页文档。多页PDF必须走浏览器打印。

### 输出文件命名规范
- {项目名}-宣传册.html / {项目名}-宣传册-v2.html / {项目名}-完整版.html
- {项目名}-预览.png / P8-{页面名}.png

---

## 客户上下文（来自 AGENTS.md）

**用户**：Carl，iMorgan（摩根），专注企业国际化人才培养22年
**客户群**：央企/国企为主（中信建设、当升科技、中交、中核、中铝等）
**业务**：企业出海英语培训、跨文化沟通、国际化人才培养、海外项目人员管理
**2026关键词**：课程体系建设、产品学习体系设计
**输出偏好**：中文为主、结构化清单、表格+矩阵、关键方法论配流程图
**价值观**：做真正能解决客户问题的解决方案、先完成再完善、凡确定事项一定能落地

---

## 快速参考

- 工具模板表单样式 → `references/tool-patterns.md`
- 宣传册（14页）结构 → `references/brochure-structure.md`
- 完整手册（30页）结构 → `references/manual-structure.md`
