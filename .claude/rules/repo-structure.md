# 仓库结构详情

Obsidian 知识库（vault），通过 Obsidian Sync 在多设备间同步，同时用 git 做版本备份。

## 两大核心文件夹

| 文件夹 | 用途 | 核心结构 |
|--------|------|---------|
| `ACT笔记-深度思考/` | 个人思考与项目执行系统 | 收件箱→索引→Action→Card→Time→storage（ACT 六层） |
| `LLM Wiki知识应用/` | 外部知识采集与萃取 | raw（原始素材）→ entities（结构化实体）→ concepts/reports（产出） |

## ACT 系统层（`ACT笔记-深度思考/`）
- **1-收件箱**：get笔记、灵感记（待处理入口）
- **2-索引**：人物/主题索引卡
- **3-Action**：Focus 聚焦承诺 / Active 活跃跟进 / Maybe 将来也许
- **4-Card**：IndexCard 索引卡 / BibCard 阅读卡 / **MainCard 核心卡（B卡，核心思维框架）**
- **5-Time**：Vision → Monthly → Weekly → Daily
- **6-storage**：归档、模板、数据视图、Beck课程

## LLM Wiki 层（`LLM Wiki知识应用/`）
- `raw/`：原始素材（公众号文章、研究报告、国别文化、培训案例、专项萃取）
- `entities/`：结构化知识实体（人物、工具、案例、竞品、训练产品、书籍萃取）
- `concepts/`、`reports/`：提炼后的概念与报告
- `方法工具箱/`：课程萃取项目模板、AI业务专家Agent

## 收件箱
- `收件箱：同步助手/`：多设备同步操作日志
  - `企业出海日报/`：每日行业动态简报
  - `Cloude Code学习/`：Claude Code 使用学习记录
  - `_processed/`：已处理的操作日志归档
- `收件箱：需求模拟/`：每日客户分析报告（按日期命名，格式 `YYYY-MM-DD-客户分析报告.md`）
