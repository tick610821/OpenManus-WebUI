![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/Shybert-AI/OpenManusAI)
![GitHub Repo stars](https://img.shields.io/github/stars/Shybert-AI/OpenManusAI)
![GitHub](https://img.shields.io/github/license/Shybert-AI/OpenManusAI)

[English](README_en.md) | 简体中文

# OpenManusX 🙋

Manus和OpenManus 非常棒，非常优秀的工作，目前OpenManus暂无前端，于是本人花了2小时开发基于Flask框架一个简单的WebUI。 🛫！

##  本项目实际上是构建一个前端页面，通过调用flask框架实现OpenManus的调用。

前端页面需要不断的优化！优化点：    
1.OpenManusX文件预览区及保存区需要支持pdf、ppt、word、excel、代码高亮的展示;    
2.右侧的大模型对话框需要进行美化，需要进行对OpenManus运行log进行优化显示，如代码高亮等;    
3.不断打磨前后端，完成自动化执行。  
<div align="center">
    <img src="./assets/1.jpg">
</div>
<div align="center">
    <img src="./assets/2.jpg">
</div>
<div align="center">
    <img src="./assets/3.jpg">
</div>

用 OpenManusX 开启你的智能体之旅吧！  


## 安装指南

1. 创建新的 conda 环境：

```bash
conda create -n OpenManusX python=3.12
conda activate OpenManusX
```

2. 克隆仓库：先进行安装OpenManus，后续安装OpenManusX的webUI就快的很

```bash
https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```
4.安装OpenManusAI,2种方式

```bash
# 1 仓库安装
https://github.com/Shybert-AI/OpenManusAI.git
cd OpenManus
pip install -r requirements.txt

# 2 将OpenManus的运行代码拷贝到app.py文件

async def main(prompt):
    agent = Manus()
    await agent.run(prompt)

```

## 配置说明

OpenManusX配置API和OpenManus一样，需要配置使用的 LLM API，请按以下步骤设置，本文配置deepseek R1模型：

1. 在 `config` 目录创建 `config.toml` 文件（可从示例复制）：

```bash
cp config/config.example.toml config/config.toml
```

2. 编辑 `config/config.toml` 添加 API 密钥和自定义设置：

```toml
## Global LLM configuration
#[llm]
#model = "deepseek-chat"
#base_url = "https://api.deepseek.com/v1"
#api_key = "sk-xxxxxxxxxxxx"
#max_tokens = 4096
#temperature = 0.6
#
## Optional configuration for specific LLM models
#[llm.vision]
#model = "deepseek-chat"
#base_url = "https://api.deepseek.com/v1"
#api_key = "sk-xxxxxxxxxxxx"


# Global LLM configuration
[llm]
model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
base_url = "https://api.siliconflow.cn/v1/"
api_key = "sk-xxxxxxxxxxxxxxxxxx"
max_tokens = 4096
temperature = 0.6

# Optional configuration for specific LLM models
[llm.vision]
model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
base_url = "https://api.siliconflow.cn/v1/"
api_key = "sk-xxxxxxxxxxxxxxxxxx"
```

## 快速启动

一行命令运行 OpenManusX：

```bash
python app.py
```

## 致谢

特别感谢 [OpenManus](https://github.com/mannaandpoem/OpenManus)
和 [browser-use](https://github.com/browser-use/browser-use) 为本项目提供的基础支持！

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Shybert-AI/OpenManus-WebUI&type=Date)](https://star-history.com/#Shybert-AI/OpenManus-WebUI&Date)
