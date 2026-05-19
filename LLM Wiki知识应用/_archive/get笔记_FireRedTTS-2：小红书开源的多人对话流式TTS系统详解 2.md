---
note_id: 1894254375535304272
title: "FireRedTTS-2：小红书开源的多人对话流式TTS系统详解"
type: link
source: "wechat"
created: 2025-11-26 20:57:42
synced_at: 2026-05-05 17:57:tags: [FireRedTTS-2, 多人对话TTS, 流式语音合成]成"]
---

🎙️ **项目背景与定位**  
- 传统TTS工具在多人对话场景存在痛点：声音串台、语调突兀、延迟高、长音频效果差  
- FireRedTTS-2是小红书团队开源的**长对话流式TTS系统**，专注解决多人对话生成问题  

✨ **核心亮点与技术突破**  
1. **自然多人对话**：支持生成**3分钟内、最多4人**的播客式对话，声音衔接丝滑  
2. **超低延迟**：L20 GPU上首包延迟仅**140毫秒**，满足实时配音场景（语音客服、虚拟主播等）  
3. **多语言能力**：开箱即用支持中、英、日等多国语言，支持**零样本语音克隆**和中英混合合成  
4. **稳定性强**：解决说话人切换不稳定问题，告别“串声”和“语调突兀”  
5. **可扩展性**：未来可通过扩展训练数据支持更长对话和更多说话人  

📝 **快速上手步骤**  
1. **下载代码**  
   - 链接：https://github.com/FireRedTeam/FireRedTTS2  
   - 命令行：`cd FireRedTTS2`  
2. **创建环境与安装依赖**  
   - 虚拟环境：`conda create --name fireredtts2 python==3.11` → `conda activate fireredtts2`  
   - 安装PyTorch：`pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu126`  
   - 项目依赖：`pip install -e .` → `pip install -r requirements.txt`  
3. **下载预训练模型**  
   - `git lfs install`  
   - `git clone https://huggingface.co/FireRedTeam/FireRedTTS2 pretrained_models/FireRedTTS2`  
4. **启动WebUI**  
   - `python gradio_demo.py --pretrained-dir "./pretrained_models/FireRedTTS2"`  

💻 **代码调用示例**  
- 初始化模型：指定预训练目录、生成类型（dialogue）和设备（cuda）  
- 定义对话文本：用`[S1]`/`[S2]`标记不同说话人  
- 音色提示：通过prompt_wav_list传入说话人声音样本（如`examples/chat_prompt/zh/S1.flac`）  
- 生成并保存音频：调用`generate_dialogue`方法，输出保存为`chat_clone.wav`
