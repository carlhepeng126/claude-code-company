---
tags: [AI, Terminal, 工作流]
author: 林大友
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489578&idx=1&sn=18422a30861ccff664dd73808dd791a0
saved: 2026-05-05 06:29
processed: 2026-05-14
id: 4900c7c9-4248-462f-b747-8ae259d24950
-
# Obsidian入门31：Terminal插件实战 — 开启你的"传送阵"

这是「Obsidian × AI」系列的"集成三部曲"之二。

## 为什么需要"手动挡"？

两个核心理由：
1. **专注**：对特定子目录（如写作文件夹）运行AI，避免全库扫描浪费Token
2. **精准**：子目录下有专属写作Skill和claude.md指令，cd进入后AI瞬间"附身"

## 配置两步走

### 第一步：安装
Obsidian插件市场搜索 **Terminal**。

### 第二步：给黑窗口注入"灵魂"

1. **找到"门牌号"**：终端输入 `npm config get prefix`（通常返回 `/opt/homebrew` 或 `/usr/local`）
2. **打"环境补丁"**：编辑 `~/.zshrc`，添加 `export PATH="$PATH:/opt/homebrew/bin"`
3. **检查"登录模式"**：插件设置中确认 Arguments 有 `--login`

核心原理：`--login` 参数让终端以真正用户的身份"登录"，`.zshrc` 中的PATH补丁是地图。地图和绿卡到位，`claude`/`gemini`/`opencode` 才能真正听指挥。

## 快捷操作

右键文件夹 → **"在此处打开终端(Open terminal here)"** → 侧边栏小黑窗自动跳转到该目录 → 直接敲 `claude` 即可让AI读取该目录下的专属技能。

## 多模型切换

在Terminal中可以自由切换：
- Claude Code：重构笔记逻辑
- Gemini CLI：Google博学多才的视角
- OpenCode：支持免费模型
- Codex：ChatGPT救急方案

核心理念：你不再是被插件定义的用户，你是指挥这些顶级AI的国王。
