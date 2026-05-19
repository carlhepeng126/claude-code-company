---
note_id: 1906960475787931288
title: "OpenClaw技能教程：公众号文章自动同步至飞书多维表格全流程"
type: link
source: "wechat"
created: 2026-04-12 20:02:20
synced_at: 2026-05-05 17:57:tags: [OpenClaw, 公众号文章同步, 飞书多维表格]步"]
---

### **🔧 核心功能概述**

**技能定义**：将公众号文章链接通过**OpenClaw**自动提取标题、正文、概要，并写入**飞书多维表格**，解决微信聊天中文章沉淀难题。  
**核心价值**：实现内容从即时通讯工具到结构化知识库的自动化迁移，提升素材整理、选题库建设、内容分析及AI再加工效率。  
**使用特性**：一次配置，长期复用，无需重复操作。

### **📋 操作步骤详解**

#### **(一) 新建飞书应用并授权**
1. **创建应用**  
   - 访问飞书开放平台（https://open.feishu.cn/app?lang=zh-CN），选择“企业自建应用”，点击“创建企业自建应用”。  
   - **关键操作**：记录生成的**App ID**和**App Secret**（应用凭证），后续配置需使用。

2. **权限配置**  
   - 进入应用“权限管理”页面，点击“批量导入/导出权限”，导入以下JSON权限配置：  
   ```json
   {  
     "scopes": {  
       "tenant": [  
         "base:table:create",  
         "base:table:delete",  
         "base:table:read",  
         "base:table:update",  
         "bitable:app",  
         "bitable:app:readonly"  
       ],  
       "user": []  
     }  
   }  
   ```
   - **注意事项**：配置完成后需“发布”应用，确保权限生效。

#### **(二) 文档授权与应用绑定**
1. **创建多维表格**  
   - 在飞书云盘中“新建”→“多维表格”，作为文章存储的目标位置。

2. **绑定应用**  
   - 进入多维表格，通过“更多”→“添加文档应用”，搜索并关联第一步创建的飞书应用。

3. **获取关键参数**  
   - 从多维表格URL中提取**FEISHU_APP_TOKEN**（表格token）和**FEISHU_TABLE_ID**（数据表ID），与前一步的App ID、App Secret共同构成4个核心参数：  

   | 参数                | 说明         | 获取方式               |  
   |---------------------|--------------|------------------------|  
   | FEISHU_APP_ID       | 飞书应用ID   | 飞书开放平台应用凭证   |  
   | FEISHU_APP_SECRET   | 飞书应用密钥 | 同上                   |  
   | FEISHU_APP_TOKEN    | 多维表格token| 表格URL中提取          |  
   | FEISHU_TABLE_ID     | 数据表ID     | 表格URL中提取          |  

   - 将参数保存为文本文档（如“～/Downloads/feishu.txt”），供OpenClaw读取。

#### **(三) 调用Skill保存文章**
1. **安装Skill**  
   - 执行命令安装技能：  
     ```  
     调用https://clawhub.ai/harven-droid/wechat-article-parser 这个skill，配置文件路径为～/Downloads/feishu.txt  
     ```  
   - 系统会自动将配置文件移动至OpenClaw的配置文件夹（.openclaw）。

2. **日常使用**  
   - 直接发送指令保存文章：  
     ```  
     调用wechat-article-parser这个skill。将我的微信文章[公众号链接]保存到飞书文档  
     ```
### **💡 补充细节**
- **社群支持**：提供“openclaw交流群6群”（含二维码），供用户交流更多玩法。  
- **理念目标**：核心追求“减少人工，提高含硅率”，即通过自动化工具提升效率。  
- **相关资源**：附8篇历史文章链接，涵盖OpenClaw安全性、数据喂养、定时任务等进阶主题。
