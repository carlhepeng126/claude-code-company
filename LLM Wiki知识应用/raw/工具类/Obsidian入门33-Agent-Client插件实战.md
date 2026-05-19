---
tags: [ACP协议, AI]
author: 林大友
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489668&idx=1&sn=33fc0c25e27381d1912908568b8d10ae
saved: 2026-05-05 06:27
processed: 2026-05-14
id: 02ee79de-d5ab-4313-899a-b91bfae7f4ff
-
# Obsidian入门33：Agent Client插件实战 — 你的全能AI辅助官

原文链接：[https://xiaoweibox.top](https://xiaoweibox.top)

这是「Obsidian × AI」系列的"集成三部曲"终章。

## 核心揭秘：什么是 ACP 协议？

**ACP (Agent Client Protocol)** — AI 时代的"普通话标准"。

以前，每个 AI 助手（如 Claude, Gemini）都有自己的脾气，它们说着不同的方言，笔记软件很难跟它们沟通。而 ACP 协议就像是一部万能翻译机，只要大家都说这套"普通话"，Obsidian 就能像插拔 U 盘一样，随时更换它的 AI 大脑。

## 为什么选这个"全能王"？

1. **一键换脑** — 同一个界面，这一刻让Claude重构笔记大纲，下一秒切到Gemini查偏门资料
2. **跨模型联动** — 让Gemini快速生成素材，再切到国产模型进行"去AI味"润色
3. **自动感知（Context）** — 自动感知工作状态，点击不同笔记时AI自动聚焦当前文稿

## 实操步骤

### 第一步：安装
使用 BRAT 插件，添加地址：`RAIT-09/obsidian-agent-client`

### 第二步：一键"点亮"AI
1. 打开Obsidian插件设置，找到 **Agent Client**
2. 找到 **「Built-in agents」** 栏
3. 找到想要的那位助手（Claude Code / Codex），点右边的 **「Auto-detect」** 按钮
4. 插件自动扫描电脑并填写路径

### 第三步：Gemini CLI配置
除Auto-detect外，需确认Arguments中已填好 `--experimental-acp`

## 核心特性

### 库即世界
默认将整个 Obsidian 库（Vault）作为项目根目录，能看穿整个知识库。

### 自动上下文
编辑某篇笔记时，对话框自动把该笔记加入上下文。直接提问，AI永远知道你在想什么。

### Session 统帅部
- 加号：开启全新对话
- 历史记录：给对话起名字，随时回溯
- Fork（分支）对话：保留原思路的同时拉出新分支测试，互不干扰

### 一键换脑
在顶部列表随时切换 Claude Code、Codex、Gemini，也支持添加自定义Agent。

### 对话即笔记（导出功能）
保存按钮一键导出完整对话（含Thinking过程）为Markdown文件，自动存入库中。

**核心理念**：让 AI 彻底消失在你的工作流中，让它成为如影随形、触手可及的"第二大脑"。
