# GBrain MCP — Claude Code 远端接入配置

## 配置信息

| 项目 | 值 |
|------|-----|
| **MCP URL** | `http://106.75.16.33/mcp/sse` |
| **Bearer Token** | `gbrain-mcp-token-2026` |
| **后端服务** | `gbrain serve` (版本 0.30.2) 通过 `fastmcp run` SSE桥接 |
| **认证方式** | Bearer Token (Authorization header) 或 Query参数 `?token=xxx` |
| **服务器外网IP** | 106.75.16.33 |

## 注册到 Claude Code

编辑 `~/.claude.json`（Windows 路径：`C:\Users\Admin\.claude.json`）：

```json
{
  "mcpServers": {
    "gbrain": {
      "url": "http://106.75.16.33/mcp/sse",
      "headers": {
        "Authorization": "Bearer gbrain-mcp-token-2026"
      }
    }
  }
}
```

注册成功后，在 Claude Code 对话中可以使用 `mcp__gbrain__*` 工具。

## 架构说明

```
Claude Code (Windows)
       ↓ HTTP SSE (Bearer Auth)
Nginx :80 (106.75.16.33)
       ↓ proxy_pass
fastmcp run (127.0.0.1:9876)
       ↓ spawn
gbrain serve (stdio MCP Server)
       ↓ 
PostgreSQL (PGLite 本地数据库)
```

## 可用工具

注册后可直接调用的 gbrain MCP 工具：

- `mcp__gbrain__search` / `mcp__gbrain__query` — 混合搜索
- `mcp__gbrain__get_page` — 读取页面
- `mcp__gbrain__put_page` — 写入页面
- `mcp__gbrain__list_pages` — 列出页面
- `mcp__gbrain__get_recent_salience` — 近期动态
- `mcp__gbrain__think` — 多跳推理
- 其他：tags, links, timeline, files, takes, jobs 等

完整列表参见 `skills_list` 中 `gbrain` 开头的工具。
