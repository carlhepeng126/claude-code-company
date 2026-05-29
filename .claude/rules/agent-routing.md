# Agent 编排与路由规则

## Agent 编排架构

三层 Agent 协作，定义在 `.claude/agents/`：

| Agent | 角色 | 决策引擎 | 模式 |
|-------|------|---------|------|
| **orchestrator** | 编排器，统一入口，三域信号检测，智能路由，跨域信号同步 | — | 信号扫描→路由→合并 |
| **intel-expert** | 情报专家 · 央企培训六维情报分析（前置情报层） | 六维对齐评分→五级分类 | 单公司/行业对比/竞品分析/空白扫描/信号查询 |
| **diagnose-client** | 企业出海培训诊断与方案 | B024 v2.2 九关决策流 | A诊断/B方案/C头脑风暴/D语料库/E跨域信号 |
| **consult-client** | 管理培训与组织咨询诊断与方案 | B025 v1.0 六步决策流 | A诊断/B方案/C头脑风暴/D语料库/E跨域信号 |

## 路由逻辑

| 场景 | 走编排器 | 直接走子Agent |
|------|:--:|:--:|
| 用户只说英语培训/管理咨询 | ✓ | - |
| 用户描述同时涉及两个域（如"海外项目经理不会带团队"） | ✓ | - |
| 用户说"完整方案""全案""双轨""语言+管理" | ✓ | - |
| 用户查询央企培训机会/竞品/行业（"看看XX有没有机会"） | ✓（优先走intel-expert） | - |
| 用户明确用 `/diagnose-client` 或 `/consult-client` | - | ✓ |
| 用户明确用 `/intel-expert` | - | ✓ |

编排器检测到情报查询信号时，优先路由到 intel-expert 出情报卡，再视情况继续路由到 diagnose/consult。原则：**宁可多走编排器**。

## Skills（触发层，`.claude/skills/`）

- `orchestrator` / `intel-expert` / `diagnose-client` / `consult-client` — 对应四个 Agent 的 Skill 触发层
- `brainstorming` — 视觉化头脑风暴辅助（含本地服务器）
- `proposal-review` — 方案审查
- `browse` — 网页浏览与内容抓取
- `web-design` / `hue` — 网页设计与设计系统

## Commands（`.claude/commands/`）

- `pass-all` — 全自动模式：不询问确认，所有操作直接执行到底
- `agents` — Agent 体系运行看板
- `aside` — 临时提问不丢上下文：`/aside <问题>`
- `learn-eval` — 会话复盘：提取可复用模式和经验，存入知识库
- `save-session` / `resume-session` — 保存/恢复会话状态
- `sessions` — 查看历史会话记录
