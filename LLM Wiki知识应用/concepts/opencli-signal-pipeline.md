---
title: OpenCLI 信号萃取管道
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [type/模型, 知识管理]
maturity: sapling
context: [内部运营, 方案设计, 课程交付]
---

# OpenCLI 信号萃取管道

> 将 OpenCLI 本地抓取的竞品信号（小红书+X/Twitter）自动萃取为知识库 entity/concept 卡片的管道。

## 架构

```
Carl本地运行 OpenCLI
       │
       ▼ (数据同步)
~/wiki/收件箱/opencli/
  ├── xiaohongshu/YYYY-MM-DD/  ← 小红书竞品搜索+创作者数据
  └── twitter/YYYY-MM-DD/      ← X/Twitter 趋势+搜索数据
       │
       ▼ (cron: 每日9:30)
.scripts/opencli-extract.py
       │
       ▼
entities/opencli-*.md     ← 竞品/趋势信号卡片
concepts/opencli-*-*.md   ← 每日信号日报
```

## 触发方式

1. **cron 自动扫描**: 每日9:30运行 `opencli-extract.py`，检查是否有新日期目录
2. **手动运行**: `python3 .scripts/opencli-extract.py [--force] [--dry-run]`

## 萃取逻辑

| 输入 | 萃取规则 | 产出 |
|------|---------|------|
| 关键词搜索结果(≥2条) | → entity 卡片（按关键词汇总） | competitor/trend signal |
| 同一作者出现≥2次 | → entity 卡片（竞品作者分析） | competitor profile |
| 每日所有信号 | → concept 卡片（信号日报） | daily summary |
| 高互动笔记(creator-notes) | → 不做独立卡片（已体现在每日日报） | aggregate signal |

## 状态追踪

使用 `~/wiki/收件箱/opencli/_extraction_state.json` 记录已处理日期，避免重复萃取。

## 关联脚本

- `.scripts/opencli-extract.py` - 萃取管道的核心脚本
- `OpenCLI信号抓取脚本-fetch-signals.py` - Carl在本地运行的数据抓取脚本

## 关联概念

- [[opencli-daily-signals-*|信号日报]]
- [[batch-extraction-pipeline|知识库批量萃取管道]]
