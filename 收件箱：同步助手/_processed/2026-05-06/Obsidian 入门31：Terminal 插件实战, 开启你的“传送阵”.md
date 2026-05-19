---
author: 林大友
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489578&idx=1&sn=18422a30861ccff664dd73808dd791a0&chksm=c5a6406b05d2ac0424004be196819412e943579b65da6ac9adea5ea9a551238329ad02c27885&mpshare=1&scene=1&srcid=0505Xb2ilkKCO7vpKbAzXsFB&sharer_shareinfo=93e707aa20f64d3feee8730bd57b58f8&sharer_shareinfo_first=93e707aa20f64d3feee8730bd57b58f8#rd
saved: 2026-05-05 06:29:tags: []助手
id: 4900c7c9-4248-462f-b747-8ae259d24950
---

公众号名称：林小卫很行

作者名称：林大友

发布时间：2026-04-22 08:09

原文链接：[https://xiaoweibox.top](https://xiaoweibox.top)

> 这是一个「Obsidian × AI」系列。
> 
> 我会从最基础的认知开始，慢慢写到资料整理、写作工作流，再到怎么把 AI 接进来。
> 
> 如果你还没看过前几篇，可以先看[Obsidian 入门30：将AI集成进Obsidian侧边栏，选哪一个](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489568&idx=1&sn=db99d74d2e210c5ace0adf197df5f0d2&scene=21#wechat_redirect)

---

上一篇，我们给三位侧边栏的“面试者”做了选型对比。

今天，我们要请出其中最自由、最硬核的那位“老兵”：**Terminal 插件**。

虽然它的长相平平无奇，就是一个黑框框，但在我心里，它是不可替代的。因为它能给你一种“掌控全世界”的自由。

---

## 为什么我们需要一个“手动挡”？

很多人不理解：既然有专门的 AI 插件，为什么还要在侧边栏装个终端？

我有两个必须用它的理由。

第一，是“专注”。我的 Obsidian 库很大，包含了我生活、工作的方方面面。但我平时花精力最多的地方，其实是那个叫 `Wechat` 的子文件夹。

如果你直接在库的根目录运行 AI，它会像个好奇宝宝一样到处乱看，既浪费 Token，又容易被一些无关紧要的文件干扰了判断。

第二，是“精准”。我在 `Wechat` 目录下定义了专门的写作、生图 Skill，还有一份专属的 `claude.md` 指令。我只有通过 `cd` 命令（还记得那个[任意门](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489550&idx=1&sn=fc5582dd5127507bbbef207d836d0747&scene=21#wechat_redirect)吗？）钻进这个特定的“写作车间”，AI 才能瞬间“附身”，变成我的首席编辑。

---

## 实操：两步跨越“配置鸿沟”

很多小白装完 Terminal 插件，兴冲冲敲下 `claude`，结果跳出一个巨大的错误：`command not found`。

那一刻，挫败感通常会让你想直接点那个“卸载”按钮。

**别怕，这是因为 Obsidian 还没拿到你电脑的“地图”。**

### 第一步：安装

在 Obsidian 插件市场搜索 **Terminal**，安装并启用。

![[笔记同步助手/images/bafbbb2aef525cffcba40c468ac6788f_MD5.png]]

### 第二步：给黑窗口注入“灵魂”

装完之后，如果你直接在侧边栏敲 `claude`，大概率会看到那个讨厌的错误：`command not found`。

这是因为 Obsidian 作为一个图形软件，它默认是“看不见”你系统里的那些高级工具的。它就像一个被关在房间里的客人，找不到去地下室工具间的路。

我们要做的，是给它画一张精确的“地图”。

#### 1\. 找到“门牌号”

打开你电脑自带的终端（注意，不是 Obsidian 里的，是系统原生的），敲下这一行：

1npm config get prefix

如果返回的是 `/opt/homebrew` 或 `/usr/local`，记住这个地址。

![[笔记同步助手/images/5bbee049babaafac16b4698b67e8264c_MD5.png]]

  

#### 2\. 打个“环境补丁”

这是最关键的一步，我们要把这个地址告诉系统的“总管”：

1.  在终端输入 `nano ～/.zshrc`，打开你的配置文件。
    
2.  划到最下面，新起一行，贴入这句代码：  
    `export PATH="$PATH:/opt/homebrew/bin"` （如果第一步返回的是别的地址，请对应修改）。
    
    ![[笔记同步助手/images/98ede798816a309009fa321ed3c59232_MD5.png]]
    
3.  按 `Ctrl + O` 保存，再按 `Ctrl + X` 退出。
    
4.  最后敲一句 `source ～/.zshrc` 让它立即生效。
    
    ![[笔记同步助手/images/dfc08165931a7a2d7a1b50d6cf446ad2_MD5.png]]
    

#### 3\. 检查“登录模式”

回到 Obsidian 的 Terminal 插件设置里：

1.  点击 **「配置 (Profiles)」** 右侧的列表图标，编辑你的默认配置。
    
2.  找到 **「参数 (Arguments)」** 这一行。
    
3.  检查一下​： 正常情况下，插件的预设应该已经帮你填好了 **`--login`**（或者 `-l`）。如果已经有了，你就不用管它；如果这一行是空的，请手动点“+”号填上去。  
    
    ![[笔记同步助手/images/ae1857d2a06117bc77fcd43926bce749_MD5.gif]]
    

> **为什么这么折腾？**：这一整套动作，其实是给了终端一张“通关绿卡”。参数里的 `--login` 负责告诉终端：请像一个真正的用户一样“登录”我的电脑。而我们刚才在 `.zshrc` 里打的补丁，则是为它准备好的“地图”。
> 
> 只有地图和绿卡都到位了，你在侧边栏里敲 `claude`、`gemini` 还是 `opencode`，它们才会真正听你使唤。

![[笔记同步助手/images/1e05ef20cd334b8fe1c81a01f555d4ac_MD5.png]]

---

## 高光时刻：瞬移进你的“车间”

一般来说，在左边侧边连，点击即可快速启动 Terminal 窗口。

在这里，你可以通过CD 命令（具体参考[Obsidian 入门28：坐标跳转，让 AI 真正“降临”你的库](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489550&idx=1&sn=fc5582dd5127507bbbef207d836d0747&scene=21#wechat_redirect)) 跳转到具体的某个子文件夹，例如写作目录。

![[笔记同步助手/images/743d5bd9507fc00da0f7c68947db0580_MD5.gif]]

  

不过，这里还有一个更直观、连设置都不用翻、CD 命令都不需要输入的办法：

1.  在 Obsidian 左侧的文件列表（File Explorer）里，找到你的 **`Wechat`** 文件夹。
    
2.  对着它点**右键**。
    
3.  选那个 **「在此处打开终端 (Open terminal here)」**。
    

**奇迹发生了**：侧边栏的小黑窗会自动跳出来，而且它的“当前位置”已经稳稳地停在了你的 `Wechat` 目录下。

![[笔记同步助手/images/cf9186fabf993094986fb63e39a78f44_MD5.gif]]

现在，你只需要敲下一句：

1claude

Claude 这一次会立刻读取你 `Wechat` 目录下的专属技能。它知道你现在的身份是一名博主，准备开始一场硬核的写作马拉松。这种“局部感知”的效率，是任何全库扫描插件都给不了的。

---

## 多模型大乱斗：在这个窗口里，你是国王

侧边栏终端最大的魅力，就在于这种“全能切换”的自由。

![[笔记同步助手/images/345e721d1037f699331b7cc4f94c633a_MD5.png]]

我平时会打一套“组合拳”：

-   Claude Code​： 虽然我加的是 MiniMax 或 GLM 的“平替油”，但它重构笔记的逻辑依然很稳。
-   Gemini CLI​： 当我需要 Google 家那种博学多才的视角时，敲一下 `gemini` 就能无缝接力。
-   OpenCode​： 因为这个插件就是电脑原生终端的镜像，所以我还可以非常方便地在这里运行 OpenCode，可以使用一些 OpenCode 提供的一些免费模型。
-   Codex​： 如果前面的都卡壳了，我还会请出 ChatGPT 的 Codex 救急。

在这个小小的侧边栏里，你不再是被插件定义的用户，你是指挥这些顶级 AI 的国王。

---

今天的作业：**成功装好 Terminal 插件，并尝试用 `cd` 命令进入一个子文件夹跑通 `claude`。**

​

ℹ️Note

如果你在 `cd` 进入文件夹时报错，记得检查一下文件夹名字的大小写，终端对这个可是非常敏感的。

别小看这个黑窗口。当你学会了在笔记侧边栏直接操控全世界的 AI，你会发现：你离“数字游民”那种随心所欲的自由，又近了一步。

下一篇，我们来聊聊那个更美观、更适合大多数人的方案：**Claudian 插件**。

动手试试，下期见！

---

## 进阶阅读

-   [Obsidian 入门30：将AI集成进Obsidian侧边栏，选哪一个](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489568&idx=1&sn=db99d74d2e210c5ace0adf197df5f0d2&scene=21#wechat_redirect)
    
-   [Obsidian 入门28：坐标跳转，让 AI 真正“降临”你的库](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489550&idx=1&sn=fc5582dd5127507bbbef207d836d0747&scene=21#wechat_redirect)
    
-   [保姆级教程：将 Gemini CLI和Claude code集成到 Obsidian](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247485994&idx=1&sn=65c2efa26a21907a43ba57634e7cdfea&scene=21#wechat_redirect)
    

  

如果这篇文章对你有帮助，欢迎一键三连（点赞、在看

转发）。另外，还有一个 Obsidian 交流群，有需要的朋友欢迎加入。

![[笔记同步助手/images/d6f2858b6d67ff7c7a1318d5ddd5a46b_MD5.jpg]]

---

![[笔记同步助手/images/c64f096b800421e310bf6b26c5667aa6_MD5.jpg|cover_image]]

Original 林大友 林小卫很行

Read more