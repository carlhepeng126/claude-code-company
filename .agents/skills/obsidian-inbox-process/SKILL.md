---
name: obsidian-inbox-process
description: |
  处理 LLM Wiki 收件箱中的文章，自动分类、生成结构化知识文件、建立双向链接。
  当用户说 "处理收件箱"、"处理这篇文章"、"整理今天的文章"、"把收件箱的文章分类"
  时触发。也用于清理 doc-* 未命名文件和批量整理知识库。
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
---

# Obsidian 收件箱处理

## 环境

- 收件箱: `收件箱：同步助手/YYYY-MM-DD/*.md`
- 知识库: `LLM Wiki知识应用/` (concepts/, comparisons/, entities/, reports/, raw/)
- ACT 系统: `ACT笔记-深度思考/`

## 处理流程

### 阶段 1：读取和分析

1. 读文章全文（frontmatter + 正文）
2. 提取核心信息：
   - 主题/领域（e.g. 出海合规、跨文化、央企人才、英语培训、行业知识）
   - 文章类型（框架模型、案例故事、政策分析、方法工具、数据报告、观点评论）
   - 关键概念词（3-5 个）

### 阶段 2：分类决策

| 类型 | 目录 | 示例 |
|------|------|------|
| 框架/模型/方法论 | `concepts/` | 跨文化信任五阶段模型 |
| 对比矩阵 | `comparisons/` | 央企出海培训模式对比 |
| 具体案例/实体/人物/书 | `entities/` | 法波坚石合资案例 |
| 综合报告 | `reports/` | 2026 出海趋势报告 |
| 原始素材/数据 | `raw/` 对应子目录 | 公众号文章、国别文化 |

### 阶段 3：生成知识文件

使用 `templates/concept-template.md` 或 `templates/entity-template.md` 生成结构化文件：

**Frontmatter 要求：**
```yaml
title: 中文名 (English)
tags: [领域, 类型, 子类]
source: 来源
original_date: 原文日期
processed: YYYY-MM-DD
aliases: [别名1, 别名2]
related_concepts: [[概念A]] [[概念B]]
```

**正文结构（concept 类）：**
- 一、定义（一句话 + 一段展开）
- 二、要点/框架（3-5 个要点）
- 三、与已有知识的关联（双向链接到现有概念文件）

**正文结构（entity/case 类）：**
- 基本信息（谁、什么、何时）
- 关键事实（3-5 条）
- 可提取的洞察

### 阶段 4：建立链接

1. 搜索 `LLM Wiki知识应用/` 中已有的相关概念文件
2. 在新文件中创建 `[[双向链接]]`
3. 如果新文件引入了新概念，评估是否需要在已有文件中回链

### 阶段 5：归档

- 将原始文章移动到 `收件箱：同步助手/_processed/` 
- 不改动原始文件名
- 在原始文件的 frontmatter 中添加 `processed_to: [[新文件路径]]`

## 批量处理模式

当用户要求批量处理时：
1. 列出待处理文章清单
2. 按主题分组（每组 5-8 篇可合并为一个概念文件）
3. 逐组处理，每组完成后请求确认
4. 同一主题的文章合并进同一个概念文件，而非每篇创建一个

## 命名规范

- 概念文件: `english-topic-name.md` (小写、连字符)
- 案例文件: `case-company-topic.md`
- 对比文件: `topic-comparison.md`
- 不使用 `doc-` 前缀（那是未命名状态）

## doc-* 清理

当发现 `doc-*` 开头的文件时：
1. 读取文件内容
2. 判断应该用什么规范名称
3. 重命名文件（用 `git mv` 或移动操作）
4. 更新所有引用该文件的双向链接
