![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/Shybert-AI/OpenManusAI)
![GitHub Repo stars](https://img.shields.io/github/stars/Shybert-AI/OpenManusAI)
![GitHub](https://img.shields.io/github/license/Shybert-AI/OpenManusAI)  
[English](README_zh.md) | 简体中文

# OpenManusX 🙋

Manus and OpenManus are great, but OpenManus currently does not have a front-end. Therefore, I spent 2 hours developing a simple WebUI based on the Flask framework, which can be called by calling OpenManus to achieve front-end calling. 🛫！


## 📑 The front-end page needs continuous optimization, plan
- OpenManusX
    - [x] Open source initial version of WebUI;
    - [ ] The preview and save areas of OpenManusX files need to support PDF ppt、word、excel、 Preview of highlighted code;     
    - [ ] The large model dialog box needs to be beautified for output, and the OpenManus runtime log needs to be optimized for display, such as code highlighting;
    - [ ] Continuously polish the front and back ends to achieve automated execution.

<div align="center">
    <img src="./assets/1.jpg">
</div>
<div align="center">
    <img src="./assets/2.jpg">
</div>
<div align="center">
    <img src="./assets/3.jpg">
</div>

Start your journey of intelligent agents with OpenManusX!


## installation guide

1. Create a new conda environment:

```bash
conda create -n OpenManusX python=3.12
conda activate OpenManusX
```

2. Clone warehouse: progressiveness install OpenManus, and the subsequent installation of OpenManusX's webUI will be very fast

```bash
https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. Installation dependencies:

```bash
pip install -r requirements.txt
```
4.Install OpenManusAI in 2 ways

```bash
# 1 Warehouse installation
https://github.com/Shybert-AI/OpenManusAI.git
cd OpenManus
pip install -r requirements.txt

# 2 Copy the running agent of OpenManus to the app.cy file

async def main(prompt):
    agent = Manus()
    await agent.run(prompt)

```

## Configuration Description

The OpenManusX configuration API, like OpenManus, requires configuring the LLM API to be used. Please follow the steps below to configure the Deepseek R1 model

1. Create a 'config. toml' file in the 'config' directory (can be copied from the example):

```bash
cp config/config.example.toml config/config.toml
```

2. Edit 'config/config. toml' to add API keys and custom settings:

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

## quick start

Run OpenManusX with one command, and then open it on the webpage http://127.0.0.1:5000

```bash
python app.py
```

## acknowledgments

Special Thanks [OpenManus](https://github.com/mannaandpoem/OpenManus)
and [browser-use](https://github.com/browser-use/browser-use) The basic support provided for this project!

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Shybert-AI/OpenManus-WebUI&type=Date)](https://star-history.com/#Shybert-AI/OpenManus-WebUI&Date)
