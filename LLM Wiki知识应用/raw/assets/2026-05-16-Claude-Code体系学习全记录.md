---
date: 2026-05-16
title: Claude Code 核心体系学习全记录
tags: [Claude Code, 学习, 团队赋能]
status: completed
---

# Claude Code 核心体系学习全记录

> 一次完整对话中覆盖的所有 Claude Code 核心概念、实操配置、业务场景应用。

---

## 一、Hooks（自动化触发器）

### 核心理解

Hooks 是**系统事件驱动的自动化程序**。不需要 Claude 理解指令，事件发生即触发，100% 执行。

### 五种主要事件类型

| 事件 | 触发时机 | 用途 |
|------|---------|------|
| `PreToolUse` | 工具执行**前** | 拦截危险操作、修改参数、注入上下文 |
| `PostToolUse` | 工具执行**成功**后 | 自动格式化、检查规范、更新索引 |
| `PostToolUseFailure` | 工具执行**失败**后 | 错误诊断、通知 |
| `PostToolBatch` | 一批工具调用**全部完成**后 | 批量 lint、合并处理 |
| `PermissionDenied` | 权限系统**拒绝**操作后 | 记录日志、通知用户 |

### 配置结构

```json
{
  "hooks": {
    "事件名": [
      {
        "matcher": "匹配的工具名（如 Edit|Write）",
        "hooks": [
          {
            "type": "command",
            "command": "执行的命令或脚本路径",
            "args": ["参数数组方式避免shell转义问题"]
          }
        ]
      }
    ]
  }
}
```

### 关键细节

- **matcher 区分大小写**：`Bash` 不是 `bash`
- **路径有空格时用 args 数组**：避免 JSON 转义问题
- **stdin 是唯一输入**：脚本用 `INPUT=$(cat)` 读取
- **退出码**：exit 0 = 放行，exit 2 = 拦截
- **Hook 脚本放 `.claude/hooks/` 下集中管理**

### 业务场景

- 方案写入 `项目归档/` 后自动检查命名规范
- 修改已交付方案前拦截确认
- 知识库文件修改后检查 Wiki 链接完整性

### 与 Rules 的区别

| | Hooks | Rules |
|---|---|---|
| 触发者 | 系统事件自动 | Claude 读取遵守 |
| 可靠性 | 100% | 概率性 |
| 适合 | 硬约束、安全检查 | 行为准则、工作流指导 |

---

## 二、Commands → Skills（已合并）

### 演进路径

旧版 Commands（`.claude/commands/`）在 2026 年已合并到 Skills v2。通过一个字段区分行为：

| 设置 | 行为 |
|------|------|
| 不设 `disable-model-invocation` | AI 自动判断触发 + 用户手动 `/xxx` |
| `disable-model-invocation: true` | **仅**用户手动 `/xxx` 触发 |

### 本质

Commands / Skills 都是 Markdown 文件，内容是给 Claude 的指令文本。区别在于：Commands 是纯手动，Skills 可以自动匹配。

---

## 三、Skills 与 Agents 的本质区别

### 两层架构

```
Skills 层（触发层 / 轻量 / ~500 tokens）
    ↓ spawn
Agents 层（执行层 / 重载 / ~20k tokens / 独立上下文）
```

### 核心差异

| | Skill | Agent |
|---|---|---|
| 体积 | ~500 tokens | ~20k tokens |
| 存在方式 | 常驻对话上下文 | 触发时 spawn，用完销毁 |
| 职责 | 匹配场景 + 告诉 Claude 调哪个 Agent | 完整决策流、诊断逻辑 |
| 项目数量 | 8个 | 3个（只配重量级的） |

### 分离原因：省 Token

3 个 Agent 如果常驻上下文，一下吃掉 60k tokens。拆成两层，平时只挂轻量 Skill，需要时才加载 Agent。

### Agent 的上下文

Agent 启动时被注入：
1. 项目 CLAUDE.md（工作方式、知识库结构）
2. Skill 传过来的用户描述 + 指令
3. Skill 目录下的 references 文件

**但不带主对话的历史包袱**，不会被聊偏的上下文带跑。

### 引用文件归属

Agent 本身只是 md 文件，引用文档（模板、案例索引等）放在对应 Skill 的 references 目录下。

---

## 四、Agent 之间的协作机制

### 架构

```
orchestrator（编排器）
    │
    ├── spawn → diagnose-client（语言培训域）
    │               └── 模式E：检测管理信号 → 写入共享索引
    │
    ├── spawn → consult-client（管理咨询域）
    │               └── 模式E：检测语言信号 → 写入共享索引
    │
    └── 共享文件：跨域信号索引.md
```

### 三种协作方式

1. **编排器调度**：orchestrator 做信号扫描 → 单域 spawn 对应 Agent / 双域并行 spawn → 合并结果
2. **跨域信号同步**：每个子 Agent 有"模式E"，完成后自检是否发现对另一个域有价值的信息 → 写入共享索引文件
3. **结果合并**：去重 → 交叉点标注 → 矛盾标注 → 优先级排序

### 子 Agent 互不直接对话

通过编排器 + 共享索引文件协作。这不同于 Agent Teams（同级并行、互相喊话）。

---

## 五、Agent Teams vs 自定义 orchestrator

| | Agent Teams（技术功能） | 自定义 orchestrator |
|---|---|---|
| 通信方式 | 同级互相发消息 | 层级：父→子，通过索引文件 |
| 适用场景 | 一个任务拆成多个并行子任务 | 先判断类型再分派专家的业务路由 |
| 典型用法 | 代码重构（前端+后端+测试并行） | 客户诊断（先判断培训/咨询再分派） |

### 判断标准

- 单一业务线、先分类再处理 → **层级路由**（orchestrator）
- 多业务线并行、彼此要协调 → **Agent Teams**
- 两者可叠加使用

---

## 六、Project 是什么

### 一句话

**你在哪个目录跑 `claude`，那个目录就是 Project。** 没有额外的创建命令。

### 配置结构

```
project-root/
├── CLAUDE.md              ← 全局指令（团队共享）
├── .mcp.json              ← MCP Server 定义
└── .claude/
    ├── agents/            ← Agent 定义
    ├── skills/            ← Skill 定义
    ├── rules/             ← 目录级规则
    ├── hooks/             ← 自动化脚本
    ├── settings.json      ← 项目级配置（可提交 git）
    └── settings.local.json ← 本地覆盖（自动 gitignore）
```

### 配置优先级（低到高）

```
Managed（系统 IT 管控）
  → User（~/.claude/，所有项目共享）
    → Project（项目 .claude/，团队共享）
      → Local（.claude/settings.local.json，仅你个人）
```

### 子 Project 不自动继承

子目录建的 Project 不会往上翻父目录的 `.claude/`。共享的方式：
1. **提到用户级**（`~/.claude/`）← 推荐
2. 子 Project 的 CLAUDE.md 手动引用父路径（不推荐）

### 何时建新 Project

三个判断标准：
- **够复杂** → 需要独立 CLAUDE.md 和 agents
- **和主业务无关** → 不污染主知识库
- **干完不用** → 不需要进 Obsidian 长期沉淀

缺任何一条，直接在现有 Project 里解决。

---

## 七、MCP（模型上下文协议）

### 核心理解

Claude 的"外接设备协议"。像 USB 让电脑接外设一样，MCP 让 Claude 接外部工具和数据源。

```
Claude Code（主机）
    │
    ├── MCP Server: filesystem ── 直接读写文件系统
    ├── MCP Server: websearch  ── 搜索客户背景
    └── MCP Server: 自定义API  ── 接内部系统
```

### 不装 MCP vs 装了 MCP

| | 不装 | 装了 |
|---|---|---|
| 读文件 | Claude 调 Bash → 读路径 → 回传 | Claude 直接 `mcp__filesystem__read_file` |
| 速度 | 慢，多轮调用 | 快，直连 |
| Token | 耗 | 省 |

### 配置要点

- MCP 定义**只能**在 `.mcp.json`（项目根目录），不能在 `settings.json` 里
- 批准用 `settings.json` 的 `enableAllProjectMcpServers: true` 或 `enabledMcpjsonServers`
- 使用绝对路径避免 PATH 问题

### 搭建记录

```json
// .mcp.json
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "/Users/carlhe/.local/node/bin/npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/carlhe/Documents/LLM Wiki"]
    }
  }
}
```

```json
// settings.local.json 相关字段
"enableAllProjectMcpServers": true,
"env": {
  "PATH": "/Users/carlhe/.local/node/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
}
```

### 注意事项

- MCP Server 是 npm 包（需要 Node.js），不是 Python 包
- DeepSeek 代理不影响 MCP，MCP 本地运行
- 配置完需要**完全退出** Claude Code 再重开，恢复会话不生效
- 生效后可见 `mcp__filesystem__*` 系列工具

---

## 八、Rules（路径规则）

### 核心理解

Rules 让规则跟目录绑定——Claude 进入某个目录操作时，自动加载对应规则。不需要在 CLAUDE.md 里塞一堆目录级指令。

### 配置方式

```
.claude/rules/
├── LLM-Wiki知识应用.md   ← 匹配 LLM Wiki知识应用/**
├── 收件箱.md              ← 匹配 ACT笔记-深度思考/1-收件箱/**
└── 项目归档.md            ← 匹配 ACT笔记-深度思考/6-storage/**
```

所有规则集中放在 `.claude/rules/` 下，靠文件内的匹配路径决定对哪个目录生效。

### 与 CLAUDE.md 的区别

| | CLAUDE.md | Rules |
|---|---|---|
| 作用范围 | 整个项目 | 特定目录 |
| 加载时机 | 始终加载 | 操作对应路径时加载 |
| 适合 | 全局指令 | 目录级行为约束 |

### 优势

- CLAUDE.md 瘦身
- 规则按需加载，省 token
- 同一目录下自动遵守，不需要 prompt 里反复提醒

---

## 九、Context 管理

### 核心问题

长对话会填满上下文窗口，需要压缩。

### 两个关键设置

```json
"autoCompactEnabled": true,
"autoCompactWindow": 300000
```

- `autoCompactEnabled`：窗口快满时自动压缩
- `autoCompactWindow`：触发压缩的阈值（字符数）

### 效果

出完整方案时对话很长，自动把前面内容浓缩成摘要，保留关键信息，腾出空间继续写。

---

## 十、Plugins（插件）

### 是什么

社区/官方发布的现成能力，装上就能用，不用从零写。

### 与你自定义体系的关系

| | 自定义 Skills/Agents | Plugins |
|---|---|---|
| 来源 | 你自己写 | 社区/官方 |
| 安装 | 手动创建 md 文件 | `/plugin install` |
| 定制 | 完全自由 | 参数可配 |

### 当前建议

现有体系已经够用，不需要急着上。发现某个需求自己写太费劲时，再去插件市场搜。

---

## 十一、完整体系总览

```
Claude Code 项目组织
│
├── 指令层
│   ├── CLAUDE.md          ← 全局指令（始终加载）
│   └── Rules              ← 目录级行为准则（按需加载）
│
├── 能力层
│   ├── Skills             ← 门面（触发+匹配，轻量常驻，~500 tokens）
│   └── Agents             ← 引擎（执行+决策，按需 spawn，~20k tokens）
│
├── 自动化层
│   ├── Hooks              ← 事件驱动的硬性自动化（100% 执行）
│   └── MCP                ← 外接工具协议（接 Obsidian、搜索等）
│
├── 管理层
│   ├── Context 自动压缩   ← 长会话不断
│   └── Project 隔离       ← 不同业务线互不干扰
│
└── 扩展层
    └── Plugins            ← 社区现成能力
```

## 最终项目文件结构

```
/Users/carlhe/Documents/LLM Wiki/
├── .mcp.json              ← MCP Server 定义
├── CLAUDE.md              ← 全局指令
└── .claude/
    ├── agents/
    │   ├── orchestrator.md
    │   ├── diagnose-client.md
    │   └── consult-client.md
    ├── skills/
    │   ├── orchestrator/SKILL.md
    │   ├── diagnose-client/SKILL.md
    │   ├── consult-client/SKILL.md
    │   └── ... (5个纯 Skill)
    ├── rules/
    │   └── LLM-Wiki知识应用.md
    ├── hooks/
    │   └── post-write-check.sh
    ├── commands/
    │   └── pass-all.md
    ├── settings.json       ← 暂未使用（用于共享配置）
    └── settings.local.json ← env / autoCompact / hooks / MCP批准
```

## 关键决策记录

1. **不建子 Project**：培训咨询业务在 LLM Wiki 一个 Project 内就够了
2. **先不上 Agent Teams**：单线路由够用，等业务线多了再考虑
3. **MCP 从 filesystem 开始**：风险最小、收益最直接
4. **Rules 从一条开始**：LLM Wiki 目录规则，后续按需加
5. **Hooks 从 PostToolUse 开始**：方案命名规范检查，最实用
