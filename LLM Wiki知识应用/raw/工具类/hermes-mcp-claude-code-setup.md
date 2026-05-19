# gbrain & Hermes MCP — Claude Code 外部连接配置

## 项目级配置 (LLM Wiki)

文件位置：`C:\Users\Admin\Documents\LLM Wiki\.claude.json`

```json
{
  "mcpServers": {
    "gbrain": {
      "type": "sse",
      "url": "http://106.75.16.33/gbrain/sse",
      "headers": {
        "Authorization": "Bearer gbrain-mcp-token-2026"
      }
    },
    "hermes": {
      "type": "sse",
      "url": "http://106.75.16.33/hermes/sse",
      "headers": {
        "Authorization": "Bearer hermes-mcp-token-2026"
      }
    }
  }
}
```

## 全局配置 (~/.claude.json)

同上，但项目级配置优先。

## 两个 MCP 的用途

| MCP | 端口 | Token | 能力 |
|-----|------|-------|------|
| gbrain | 9876 | gbrain-mcp-token-2026 | 知识库读写、搜索、图谱 |
| hermes | 9877 | hermes-mcp-token-2026 | 服务器终端、文件、web搜索、浏览器 |

## 架构

```
Claude Code (Windows)
  ├── gbrain MCP → http://106.75.16.33/gbrain/sse → nginx :80 → gbrain :9876
  └── hermes MCP → http://106.75.16.33/hermes/sse → nginx :80 → fastmcp :9877 → hermes mcp serve
```

两个SSE endpoint都通过nginx auth验证（Bearer Token），访问日志记录在服务器上。

## 协作工作流示例

1. Claude Code (本地) 通过 gbrain MCP 读写知识库
2. Claude Code 通过 hermes MCP 调用服务器工具：
   - 在服务器上执行命令
   - 访问服务器网络/浏览器
   - 读写服务器文件
   - 调度服务器上的 cron 任务
3. Hermes (服务器上的我) 通过本地的 gbrain CLI 操作知识库
4. 两个 Agent 通过 gbrain 共享信息
