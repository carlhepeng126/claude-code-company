---
title: 出海日报信号系统
created: 2026-05-10
type: concept
tags: [type/模型, 出海战略]
maturity: sapling
context: [方案设计, 课程交付]
related_concepts: 
---

# 出海日报信号系统

> 每日 08:00 由考恩触发器 `daily-search.py` 驱动，扫描 23 路信号源（18 路 RSS + 5 路 HTML 抓取），输出高确信度企业出海信号，自动匹配央国企实体，最终落地飞书群 + Obsidian 收件箱 + Dashboard。

## 核心架构

```
08:00 cron
 → daily-search.py（搜索 + 央国企匹配）
 → 深度解析（x-reader Playwright，前5篇36氪）
 → AI 策展（按情报线排序 + 行动建议）
 → 保存 Obsidian（收件箱：企业出海日报）
 → 推送飞书群（可选）
```

## 情报线分类

23 路信号源按 Carl 业务链分为 6 条情报线：

| 情报线 | 信号源 | 优先级 |
|--------|-------|:------:|
| 🌍 **外派管理** | Crown World Mobility | 🔴高 |
| 🇨🇳 **出海动态** | Technode, 36氪, 一带一路网 | 🔴高 |
| 👥 **企业用人** | Indeed Hiring Lab, HR Dive, Personnel Today | 🟡中 |
| 🎓 **培训趋势** | Training Industry, CLO, Training Magazine | 🟡中 |
| 📡 **商业参考** | TechCrunch, HN, 钛媒体 | 🟢低 |
| 🏛️ **央企动态** | 兵器工业集团, 国家电投 | 🔴高 |

## 信号源清单

**RSS 源（18 路）：** 36氪、HN、钛媒体、创业邦、Training Industry、Tech in Asia、TechCrunch、HR Dive、Training Magazine、CLO、HRE、Inc.com、Fast Company、腾讯研究院、Indeed Hiring Lab、Crown World Mobility、Technode、Personnel Today

**HTML 抓源泉（5 路）：** 一带一路网（NUXT 解析）、兵器工业集团（正则）、国家电投（GBK 解码）、矿冶集团 ❌（JS 动态渲染）、中国电建 ❌（JS 动态渲染）

详见 `[[LLM Wiki知识应用/concepts/intelligence-collection-pipeline|情报搜集链路设计]]`。

## 央国企实体匹配

`daily-search.py` 内置 50+ 条 SOE 匹配规则（按长度降序匹配），覆盖基建、科技通信、交通、能源、出海民企等大类。新增实体直接在脚本的 `SOE_ENTITIES` 列表尾部追加。

## 关键约束

- **不**用 `web_search` 或 `browser_navigate` 替代脚本
- **不**编造具体 URL（AI 知识补充只给框架）
- 36 氪 RSS 质量最高但出海相关信号每日 0-3 条正常
- Training Industry 内容时效性差（混入 2 年+前的文章），需检查日期
- **格式变更** — 信号源网站改版时爬虫失效 → 日报空白；需同步更新爬虫和 Dashboard 解析正则

## 输出格式

每条信号格式：
```
[⚡|📡|🏛️] [来源] — [标题摘要]
→ 发现：[具体发现]
→ 关联央国企：[公司名或无]
→ 🔗 [来源链接]
→ ⚡ Carl能用：[1-2 句业务关联]
```

保存路径：`~/wiki/收件箱：同步助手/企业出海日报/企业出海日报-YYYY-MM-DD.md`
