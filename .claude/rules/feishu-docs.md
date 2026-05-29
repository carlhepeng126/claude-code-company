# 飞书文档处理规范

当用户在飞书对话中分享飞书文档链接时，**必须**用 `lark-cli` 一次性拉取全文到临时文件，**禁止**一层层读 block 节点：

```bash
lark-cli docs +fetch --doc "<飞书文档URL>" --api-version v2 --format pretty > /tmp/feishu-doc.md
```

然后直接 `Read /tmp/feishu-doc.md` 获取全文。这样可以避免飞书文档 block 树带来的多级菜单导航问题。

如果 `docs +fetch` 报权限错误，提示用户在飞书文档里把机器人添加为协作者。
