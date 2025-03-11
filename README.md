![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/Shybert-AI/OpenManusAI)
![GitHub Repo stars](https://img.shields.io/github/stars/Shybert-AI/OpenManusAI)
![GitHub](https://img.shields.io/github/license/Shybert-AI/OpenManusAI)

[English](README_en.md) | 简体中文

# OpenManus-WebUI 🙋

&nbsp;&nbsp;&nbsp;&nbsp;Manus和OpenManus 非常棒，非常优秀的工作，目前OpenManus暂无前端，于是本人花了2小时开发基于Flask框架一个简单的WebUI。 项目实质上是通过flask框架构建一个前端页面，进行OpenManus的调用，并对OpenManus生成的文件进行预览。
# News
- 2025-03-11 OpenManus-WebUI文件预览区支持HTML、PDF、HTML、CODE的预览。ppt、word、excel目前暂不支持预览，可以下载到本地。可以自行采用OnlyOffice Document Server或者Google Docs Viewer进行的预览。
- 2025-03-08 开源初版WebUI

## 📑 前端页面需要不断的优化，计划
- OpenManus-WebUI
    - [x] 开源初版WebUI
    - [x] OpenManus-WebUI文件预览区及保存区需要支持pdf、ppt、word、excel、代码高亮的预览;    
    - [ ] 大模型对话框需要对输出进行美化，需要对OpenManus运行log优化显示，如代码高亮等;    
    - [ ] 不断打磨前后端，完成自动化执行。

## WebUI_V2
<div align="center">
    <img src="./assets/pdf.jpg">
</div>
<div align="center">
    <img src="./assets/html.jpg">
</div>
<div align="center">
    <img src="./assets/code.jpg">
</div>

## WebUI_V1
<div align="center">
    <img src="./assets/1.jpg">
</div>
<div align="center">
    <img src="./assets/2.jpg">
</div>
<div align="center">
    <img src="./assets/3.jpg">
</div>


## OpenManus-WebUI 使用方式一：（直接在已有的OpenManus环境上操作）：
   1.WebUI_v1和WebUI_v2目录是采用flask框架部署的前端页面，通过python app.py就可以启动。    
   2.OpenManus安装部署：    
      
       按照https://github.com/mannaandpoem/OpenManus.git 进行安装OpenManus。然后将WebUI_v2中的static和templates拷贝到OpenManus的项目中，然后将main.py中函数的调用方式引入到app.py中，即可实现OpenManus的Web调用。如下引用：  
 
   3.适配代码,核心代码如下，参考项目中的app.py对OpenManus中的main.py进行修改。
    ```python

    async def main(prompt):
        agent = Manus()
        await agent.run(prompt)
    ```

##  OpenManus-WebUI 使用方式二：（克隆该工程）：

1. 创建新的 conda 环境：

```bash
conda create -n OpenManus python=3.12
conda activate OpenManus
```

2. 克隆仓库：
```bash
git clone https://github.com/Shybert-AI/OpenManus-WebUI.git
cd OpenManus-WebUI
```
4. 安装依赖：
pip install -r requirements.txt

## 配置说明

OpenManus-WebUI配置API和OpenManus一样，需要配置使用的 LLM API，请按以下步骤设置，本文配置deepseek R1模型：

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

一行命令运行OpenManus-WebUI：

```bash
python app.py
```
## 欢迎大佬提出宝贵的建议和意见，提Issues，会不断进行优化和实现。
## 联系与交流

### 联系作者
- **邮箱**：854197093@qq.com
- **QQ群**：1029629549

### 打赏作者
<br/>
<div align="center">
<p>打赏一块钱支持一下作者</p>
<div align="center">
    <img src="./assets/dashang.jpg">
</div>
</div>

## 致谢

特别感谢 [OpenManus](https://github.com/mannaandpoem/OpenManus)
和 [browser-use](https://github.com/browser-use/browser-use) 为本项目提供的基础支持！

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Shybert-AI/OpenManus-WebUI&type=Date)](https://star-history.com/#Shybert-AI/OpenManus-WebUI&Date)
