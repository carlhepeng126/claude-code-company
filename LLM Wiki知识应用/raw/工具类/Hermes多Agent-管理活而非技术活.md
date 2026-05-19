---
tags: [AI, Discord]
author: 林月半子聊AI
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzU4MjY5NTc4OQ==&mid=2247499297&idx=1&sn=7db7f2f709e45d71545c76ad93e28b38
saved: 2026-05-06 09:59
processed: 2026-05-14
id: d18f39b0-a92d-48e5-b1bb-7701a75a3ace
-
# 搞完 Hermes 多 Agent 我才发现，这根本不是技术活，是管理活

公众号名称：林月半子的AI笔记
作者：林月半子聊AI
发布时间：2026-04-20

当 Hermes 出来的时候，好多人问我多 Agent 之间的协作是怎么玩的。周末我找了时间自己做了一把实践，原本以为会很顺利，没想到中间翻了好几次车，最后硬是一个坑一个坑填过来的。

## 核心认知：多Agent本质是管理问题

协作是能力的放大器，不是补丁。如果单个 Agent 本身是个废柴，拉三个废柴来协作，结果就是三倍的废柴。SOUL.md 写细、skills 配齐、模型选对，把 Agent调教好，这是多 Agent 能跑的前提。

## Profile：多Agent的基础

Hermes 的 profile 是完全独立的 AI 分身，每个 profile 有自己的 config.yaml、.env、SOUL.md、独立的 memory、独立的 skills、甚至独立的 gateway 进程。

进程级隔离的好处：即便某一个 agent 挂了，也完全不影响其他 agent 继续干活。

克隆策略三档：
- 空白创建：从零搭建完全独立的agent
- `--clone`：复制 config.yaml、.env、SOUL.md，记忆和session全新（多Agent场景首选）
- `--clone-all`：连memory、sessions、skills、cron jobs全拷贝

## 三人小组搭建

- 林小墨 (Ink) —— 文案与笔记整理专家
- 林小探 (Search) —— 搜索与调研专家
- 林小管 (Admin) —— 任务分发与调度员

这个组合对应"查资料 → 写笔记 → 归档"工作流。

## 选Discord而非飞书的原因

飞书群不支持 bot 被 @。多 Agent 协作最核心的动作就是"一个 agent @ 另一个 agent 来接力"，飞书这条路直接堵死。Discord 在这方面开放得多。

## 实战中的三个关键坑

### 坑1：没@，直接就结束了
LLM 理解"林小探是团队里的人"，但不知道在 Discord 里要真正"叫醒"对方需要 `<@用户ID>` 格式。
解决：在花名册里直接把每个人的Discord ID挂在名字后面，并严格区分计划阶段（纯文字）和执行阶段（<@ID>）。

### 坑2：任务结束后停不下来（死循环）
Bot之间互相触发的死循环——admin发"任务完成👍"，小墨响应"好的👋"，admin又响应"收到🎉"……
解决分三层：
1. DISCORD_ALLOW_BOTS=mentions（只响应显式@）
2. replied_user: false（关掉reply自带的隐式mention）
3. SOUL.md终止协议（明确终结词"【任务结束】"、禁止冗余消息、禁止再次@）

### 坑3：同时@两个人
admin 一上来同时 @ 林小探和林小墨，结果两个bot同时干活，林小墨拿不到调研结果只能瞎写。
解决：在SOUL.md里强制时序规范——逐一唤醒，必须等前一个明确回复"任务完成"后再@下一个。

## 核心结论

多 Agent 到底是个技术问题还是管理问题？
- profile 给你的是工位
- Discord 给你的是会议室
- 真正让三个 AI 像团队一样跑起来的，是那份被你一次次打磨的 SOUL.md

每一个坑本质都不是技术bug，是管理漏洞：
- 坑1没@ → 下属不知道该找谁汇报
- 坑2停不下来 → 没有明确的项目终结机制
- 坑3同时@ → 任务分派时序混乱

过去我们做不好多Agent，不是LLM不够聪明，是我们没把AI当员工来管理。
