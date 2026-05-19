---
author: 某白123
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYyNTQ0MTgwMQ==&mid=2247483958&idx=1&sn=4a076ba6990109eb6509e521d98f3bfe&chksm=f1105c77ea661df44f43065092b6dd8afb1bd307f23a30e6972df7867ffd6e0cd4d9b5dfd230&mpshare=1&scene=1&srcid=0516Ge88eKbNdlYGBCbOv7M2&sharer_shareinfo=f3fa3e6176f4279b66248384ccd5e18f&sharer_shareinfo_first=f3fa3e6176f4279b66248384ccd5e18f#rd
saved: 2026-05-16 08:03:33
tags:
  - 笔记同步助手
id: 155acd65-2e83-472b-9d12-140e37ed214f
---

公众号名称：ferlich

作者名称：某白123

发布时间：2026-03-23 14:45

# 上一篇的文章分享了一些Claude Code的教程，得到了很多人的支持。在此再次分享一些能够提高Claude Code工作效率的设置和指令。

# 先关注一下吧：

# 一、基础设置

## 1\. 全自动模式，告别反复确认

每次运行Claude都要输入

```
claude --dangerously-skip-permissions
```

但这个指令实在是太长了，根本记不住

Linux/Mac用户：​可以通过在shell里面利用alias设置别名。​在～/.bashrc或～/.zshrc加上这行：

```
alias ccauto='claude --dangerously-skip-permissions'
```

然后执行source ～/.bashrc，之后只需输入ccauto就能一键启动全自动模式。

Windows用户：新建一个ccauto.bat文件，内容如下：

```
@echo off
claude --dangerously-skip-permissions %*
```

把这个文件放在

```
C:\Program Files\nodejs
```

（或其他在PATH里的目录），然后在终端输入ccauto即可。

⚠️ 注意：全自动模式会跳过所有权限确认，适合你完全信任Claude的场景。如果还不放心，建议先用普通模式熟悉一下。

## 2\. 装上HUD，实时掌控上下文

Claude code最重要的一点是上下文管理。默认状态下，你看不到还剩多少上下文、Agent跑到哪一步了等关键信息。

这时候就需要一个HUD（抬头显示器），让你对一切尽在掌握：

![](https://relay-1.bijitongbu.site/p/017c6219e700923491253dc762d77e5f.png)

三步安装：

## 1.添加插件市场

```
/plugin marketplace add jarrodwatts/claude-hud
```

## 2\. 安装插件：

```
/plugin install claude-hud
```

2.运行配置：

```
/claude-hud:setup
```

用空格键选择你想在HUD上显示的信息，点submit即可

![](https://relay-1.bijitongbu.site/p/4bcf80163a69a9dfc23386b845230c2f.png)

HUD会实时显示上下文用量、工具动态、Agent状态和任务进度。如需调整显示内容，运行

```
/claude-hud:configure
```

有三种预设可选：Full、Essential、Minimal。

​

# 二、进阶指令

## 01 /btw — 旁路提问，不打断主任务

Claude正在跑一个长任务，你突然想问个无关问题——“那个配置文件在哪个目录？”一旦问出去，Claude会停下来回答，上下文里多了一段无关对话，后续执行可能就跑偏了。

解决方案：/btw（by the way的缩写，意思是”顺便说一下“）

```
/btw 我在哪个文件夹？
```

![](https://relay-1.bijitongbu.site/p/63939facfc60a42aed38ec84d2806095.png)

Claude 会在独立进程中回答问题，与主任务并行运行。答案内容不会进入对话历史，不影响主线任务，保持上下文干净。按空格键，回车或者Esc退出。同时由于复用当前提示缓存，几乎不消耗额外 token。

## 02 /rewind — 智能回退

让Claude尝试一个新方案，跑完发现效果不理想，想回退。以前的逻辑是全量撤销——讨论记录和代码改动全没了。

解决方案：按两下Esc或/rewind

弹出选择菜单后，你可以选择：

## 1\. 代码 + 对话一起回退

## 2\. 只回退对话（保留代码）

## 3\. 只回退代码（保留对话）

4\. 压缩上下文释放空间

![](https://relay-1.bijitongbu.site/p/8d8d1f65ae501d1c6f8db1ecb90de3ef.png)

最实用场景：实验失败后只回退代码，保留讨论脉络。Cl使用习惯

03/insights — **分析你的使用习惯**

用了几个月Claude Code，不知道自己用得对不对、哪里有优化空间。

解决方案：/insights

Claude Code会生成一份报告，分析你过去一个月的使用情况：最常触发的命令、重复操作模式、可优化空间，并推荐适合你的自定义命令和Skills。

![](https://relay-1.bijitongbu.site/p/beed9b67a91679eb7e74e1915da88a0c.png)

报告包含数据统计、具体使用建议，以及异常操作的记录。建议每月运行一次，重新审视操作习惯。

## 04 /simplify — 代码审查

运行/simplify后，Claude Code 会同时启动三个并行Agent，分别从以下三个维度审查最近的代码改动：

## 1\. 代码复用 - 找重复造轮子

2\. 代码质量 - 找可简化的写法

## 3\. 运行效率- 找性能浪费

三路并行执行后汇总结果，指出可优化的地方。适合在每个阶段性功能迭代完成后执行。

典型场景：每完成阶段性功能迭代后运行，相当于三个同事同时审查代码。

​

## 05 /branch — 对话分支

Claude刚帮你梳理完方案，你想试两种不同的实现路径，又不想丢掉当前的讨论积累。

解决方案：/branch（原名为/fork，旧命令仍可用）

功能：把当前对话复制一份，开出一条新会话，原有的不受影响。

与/rewind的区别：

-   /rewind是回退到过去
    
-   /branch是同时向多个方向推进
    

## 06 /loop — 定时循环执行任

部署服务后想每5分钟检查一下状态，之前得自己盯着或者写脚本轮询。

解决方案：/loop \[间隔时间\] \[任务描述\]

```
/loop 5m 检查部署状态 #每五分钟执行一次检查
/loop 20m /review-pr 1234 #每20分钟自动帮你审一次PR
下午三点提醒我push #一次性提醒
```

默认间隔为 10 分钟。Claude 会将自然语言转换为 cron 表达式，按设定间隔反复执行。执行结果直接保留在对话上下文中，Claude 可根据每次结果做出判断和后续操作。

特点：

-   执行结果留在上下文，Claude 可基于结果操作
    
-   任务3天后自动过期，防止遗忘循环
    
-   ## 会话级别，关终端即失效
    

## 07 /remote-control — 用手机远程操控终端

离开电脑还想继续推进任务怎么办？ 运行/remote-control（简称/rc）

运行后会生成一个 URL，用手机打开后，终端中的 Claude Code 会话会映射到手机屏幕上。两端同步操作：手机发指令，终端显示；终端有输出，手机实时刷新。对话历史在两台设备上保持一致。

代码始终在本机运行，文件系统、MCP 服务器、项目配置等全部留在本地，手机仅作为操作窗口，不持有任何数据。

## 08 /export — 导出对话，保留思考过程

和Claude围绕一个方案讨论了半小时，中间有大量权衡、否定、转折和结论。这些推导过程不保存，下次等于从零开始。

解决方案：/export

当前会话的全部内容导出为一个Markdown文件。

两个用法：

1\. 作为新会话的上下文喂进去2. 交给其他工具（比如Codex）做交叉验证——让不同AI互相审查，发现单一视角下容易忽略的问题

# 写在最后

这8个命令不，我最推荐先上手的三个：

1\. /simplify\`— 代码质量立竿见影

2\. /loop — 部署监控不用人盯

3\. HUD — 上下文透明了，心里有底

如果你发现了哪些好用的命令或用法没有在这里提到，欢迎留言告诉我。

---

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ziavPxIp40WrSXhTP6zan7JgdzCVv6Vct8iaY3MxRrBtBHTtyGDuNaWaup9brlUI3rKAR3ynGzGP9xC81l7PdFyiaEEKSACTACYCw17yR04a0I/0?wx_fmt=jpeg)

Original 某白123 ferlich

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/35f61aa6_1778889812368?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzYyNTQ0MTgwMQ%3D%3D%26mid%3D2247483958%26idx%3D1%26sn%3D4a076ba6990109eb6509e521d98f3bfe%26chksm%3Df1105c77ea661df44f43065092b6dd8afb1bd307f23a30e6972df7867ffd6e0cd4d9b5dfd230%26mpshare%3D1%26scene%3D1%26srcid%3D0516Ge88eKbNdlYGBCbOv7M2%26sharer_shareinfo%3Df3fa3e6176f4279b66248384ccd5e18f%26sharer_shareinfo_first%3Df3fa3e6176f4279b66248384ccd5e18f%23rd&s=obsidian)