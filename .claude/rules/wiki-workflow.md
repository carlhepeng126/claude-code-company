# LLM Wiki 运行机制与互通规则

## Wiki 四层操作

详见 `LLM Wiki知识应用/SCHEMA.md`：

| 层级 | 触发条件 | 目标 |
|------|---------|------|
| **Ingest（摄入）** | 有新资料到达 | 提取价值 → 更新或创建 Wiki 页面 → 维护索引和链接 |
| **Query（查询）** | 跨页面综合问题 | 检索多个页面 → 综合回答（带引用）→ 标注矛盾 |
| **Archive（归档）** | Query 产生有价值结论 | 存回知识库 → 双向关联 → 越用越丰富 |
| **Lint（健康度审计）** | 每次 Ingest 后 / 每月 | 检查孤立页面、过时内容、悬空链接、index 同步 |

## 默认工作流

**all output → wiki first。** 所有为 Carl 生成的内容（报告、分析、方案、总结）必须摄入到 Wiki，要么新建页面，要么更新现有页面。Wiki 是唯一真相源，不入库不算完成。

例外：一次性回复、快速确认、临时数据。

## ACT ↔ LLM Wiki 互通规则

1. **ACT 项目 → Wiki**（项目启动时）：ACT 项目卡片必须包含 `📎 知识库关联` 区块，关联 2-3 篇最有价值的 Wiki 素材
2. **Wiki → ACT**（反向标注）：entities/concepts 页面的 frontmatter 中 `related_projects` 字段标注哪些项目用了该知识
3. **项目交付 → 知识沉淀**（项目完成后）：从 ACT 萃取出 entity 存入 LLM Wiki，格式为 `cases-<项目类型>.md`
