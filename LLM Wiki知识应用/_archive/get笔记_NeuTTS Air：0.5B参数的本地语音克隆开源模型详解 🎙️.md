---
note_id: 1894254021200506560
title: "NeuTTS Air：0.5B参数的本地语音克隆开源模型详解 🎙️"
type: link
source: "wechat"
created: 2025-11-26 20:52:12
synced_at: 2026-05-05 17:57:tags: [开源项目, 本地AI模型, 语音克隆]目"]
---

### 项目核心亮点
- **轻量高效**：基于Qwen 0.5B语言模型+NeuCodec神经编解码器，参数仅0.5B却实现SOTA级语音合成效果
- **设备友好**：支持GGML/GGUF量化格式，普通笔记本、手机甚至树莓派可流畅运行
- **快速克隆**：仅需3-15秒参考音频即可复刻音色语调（需单声道、16-44kHz采样率、低噪音）
- **隐私安全**：完全本地部署，数据不经过云端；生成音频内置Perth水印确保可追溯性
- **社区热度**：发布数天获2.1k+ GitHub Star，登顶HuggingFace热门榜

### 关键技术架构
- **模型基础**：轻量级LM（语言模型）+Codec（神经音频编解码器）组合
- **部署格式**：GGML/GGUF量化确保低资源设备兼容性
- **克隆要求**：参考音频需满足单声道、16-44kHz采样率、3-15秒时长、低背景噪音
- **隐私保护**：本地推理杜绝数据泄露，内置水印防止技术滥用

### 本地部署实操（Docker CPU版）
```bash
# 1. 安装依赖工具
apt install git espeak
# 2. 克隆项目
git clone https://github.com/neuphonic/neutts-air.git
# 3. 安装Python依赖
cd neutts-air && pip install -r requirements.txt
# 4. 语音克隆示例（需替换为实际音频文件）
python -m examples.basic_example \
  --input_text "My name is Dave, and um, I'm from London" \
  --ref_audio samples/dave.wav \
  --ref_text samples/dave.txt
```
### 资源链接
- GitHub仓库：https://github.com/neuphonic/neutts-air
- HuggingFace在线试玩：https://huggingface.co/spaces/neuphonic/neutts-air
