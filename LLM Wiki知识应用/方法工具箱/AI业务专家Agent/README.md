---
tags: [AI, agent, 索引]
created: 2026-05-15
---

# AI业务专家Agent · 项目文件索引

> B024 v2.2 决策流为核心的诊断→方案一体化Agent。

## 文件结构

```
AI业务专家Agent/
├── README.md                    ← 你在这里
├── 01-准备计划.md                ← 原始验证计划（四周节奏）
├── 02-诊断输出模板.md            ← 18字段诊断卡 + 评分标准
├── 03-测试用例-10个.md           ← 10个匿名化测试输入
├── 04-标准答案.md (v2.1)        ← 10个用例的标准诊断（待Carl审核）
├── 诊断萃取/
│   ├── 中交海外项目.md            ← 中交需求诊断萃取（完整）
│   ├── 当升科技.md                ← 当升需求诊断萃取（完整）
│   └── 中海油服.md                ← 中海油服需求诊断萃取（完整）
└── 黄金案例/
    └── 中核二三.md                ← 单次培训型黄金案例（完整）
```

## 核心卡

| 卡片 | 位置 | 说明 |
|------|------|------|
| **B024 v2.2** | `核心卡/B024-企业出海培训需求诊断决策流.md` | 9关/6驱动/七轨/四层架构/混元学习 |
| B016 | `核心卡/B016-央企出海培训方案设计框架-中原项目萃取.md` | 短板覆盖矩阵+师资四角色 |
| B017 | `核心卡/B017-从单次培训到持续服务-当升项目萃取.md` | 三阶段路径+二次开发条件 |
| B008 | `核心卡/B008-客户需求场景化拆解.md` | 场景挖掘方法论 |
| B023 | `核心卡/B023-央企人才规划培训产品映射.md` | R.I.S.E.+六大产品线 |

## Agent 技能文件

| 文件 | 位置 |
|------|------|
| SKILL.md | `.claude/skills/diagnose-client/SKILL.md` |
| 诊断卡模板 | `.claude/skills/diagnose-client/references/diagnosis-card-template.md` |
| 方案结构 | `.claude/skills/diagnose-client/references/proposal-structure.md` |
| 报价速查 | `.claude/skills/diagnose-client/references/pricing-quick-ref.md` |
| 案例索引 | `.claude/skills/diagnose-client/references/case-index.md` |

## 验证数据源

| 来源 | 说明 |
|------|------|
| `raw/培训案例/` | 70+央企培训公开报道 |
| `raw/专项萃取/客户痛点归纳与课程大纲合并方案.md` | 20+客户真实痛点 |
| `raw/get笔记/` | 客户沟通会议记录（8+篇用于调研） |
| `D:/摩根客户/2025年/` | 60+真实方案文档 |
| `D:/摩根客户/2026年/` | 33个客户文件夹 |

## 使用方式

在 Claude Code 中输入 `/diagnose-client` 或直接说"诊断客户"、"出方案"。
