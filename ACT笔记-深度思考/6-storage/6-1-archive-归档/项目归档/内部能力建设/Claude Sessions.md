# AI Toolkit Windows 安装

```powershell
# 1. 先确保目录存在
New-Item -ItemType Directory -Path "$env:USERPROFILE\.claude\skills" -Force

# 2. 克隆仓库
git clone https://github.com/meitianwang/ai-tookit.git $env:USERPROFILE\ai-tookit

# 3. 创建目录链接
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-tools" -Target "$env:USERPROFILE\ai-tookit\claude-code\skills\session-tools"
```
