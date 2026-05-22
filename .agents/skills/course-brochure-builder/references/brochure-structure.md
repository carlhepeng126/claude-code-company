# 14-Page Brochure Structure

用于推广课程/培训产品的宣传册。精炼、有冲击力、每页一个核心信息。

## 页面结构

| 页码 | 类型 | 内容 | 背景色 |
|------|------|------|--------|
| 01 | 封面 | 标题+副标题+金字塔线条图+机构名 | 深蓝 |
| 02 | 痛点页 | 5张痛点卡片（hero深蓝区+网格区） | 米白+深蓝hero |
| 03 | 核心模型 | 四层金字塔信息图（选育防策） | 米白+深蓝header |
| 04 | M1详解 | 选拔模块：四维胜任力+八步流程 | 米白+深蓝hero |
| 05 | M2详解 | 培养模块：三阶段时间轴 | 米白+深蓝hero |
| 06 | M3详解 | 合规模块：三层防线+风险表 | 米白+深蓝hero |
| 07 | M4详解 | 策略模块：四象限区域卡片 | 米白+深蓝hero |
| 08 | 工具总览 | 14套核心工具表格 | 米白 |
| 09 | 文档地图 | 五阶段时间轴+成熟度自评 | 米白 |
| 10 | 课程交付 | 三天课程卡片+学员分层+师资组合 | 米白 |
| 11 | 实施路线 | 三阶段渐进路线（层叠色块） | 米白 |
| 12 | 案例 | 3个企业场景案例卡片 | 米白 |
| 13 | 关于我们 | 机构介绍+核心能力 | 深蓝 |
| 14 | 封底 | 金句+迷你金字塔+版权 | 深蓝 |

## 页面CSS类速查

- 封面：`.page-cover`
- 痛点页：`.page-pain` > `.pain-hero` + `.pain-grid` > `.pain-item` + `.pain-badge`
- 金字塔页：`.page-pyramid` > `.pyramid-header` + `.pyramid-body` > `.pv-tier`
- 模块页：`.page-module` > `.mod-hero` + `.mod-content` + `.mod-footer`
- 工具表：`.page-tools` > `.tools-table`
- 文档地图：`.page-docmap` > `.doc-timeline` > `.dt-phase`
- 课程交付：`.page-course` > `.day-row` > `.day-card`
- 实施路线：`.page-roadmap` > `.road-block-v2`
- 案例：`.page-cases` > `.case-card-v2`
- 关于：`.page-about` (深蓝底)
- 封底：`.page-back` (深蓝底)

## 设计要点

- 每页底部页码使用 `.page-num`（浅色页）或 `.page-num.light`（深色页）
- 模块页的hero区使用巨幅水印数字 `.mod-mega`
- 痛点页的hero区使用金黄色装饰三角形
- 金字塔页使用渐变色连接线
- 封面和封底使用圆形装饰线增加层次
