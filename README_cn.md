# Langchain-dev-utils 示例项目

## 项目概述

本示例项目演示了如何利用 `langchain-dev-utils` 提供的工具与抽象，高效构建两类典型智能体系统：
- **单智能体（Simple Agent）**：适用于端到端的简单任务自动化。
- **主管-多智能体架构（Supervisor-Multi-Agent）**：通过一个主管协调多个专业智能体，适用于需分工、规划与迭代的复杂场景。

## 项目结构

```
langchain-dev-utils-example/
├── src/                          
│   ├── agents/                   
│   │   ├── __init__.py           
│   │   ├── simple_agent/        
│   │   │   ├── __init__.py       
│   │   │   ├── agent.py         
│   │   │   └── context.py        
│   │   └── supervisor/           
│   │       ├── __init__.py       
│   │       ├── supervisor.py    
│   │       └── subagent.py      
│   └── utils/                    
│       ├── __init__.py           
│       ├── models.py             
│       └── register.py          
├── .env.example                  
├── .gitignore                    
├── .python-version               
├── LICENSE                       
├── README.md                     
├── README_cn.md                  
├── langgraph.json               
├── pyproject.toml               
└── uv.lock                    
```

## 安装步骤

1. 克隆此仓库：
```bash
git clone https://github.com/TBice123123/langchain-dev-utils-example.git
cd langchain-dev-utils-example
```

2. 使用 uv 安装依赖：
```bash
uv sync --all-groups
```

3. 配置环境变量：
```bash
cp .env.example .env
```

编辑 `.env` 文件，添加您的 API 密钥(需要 `OpenRouter` 和 `Tavily` API 密钥)
```
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 使用方法

### 通过 LangGraph CLI 运行

项目已配置为与 LangGraph CLI 兼容。使用以下命令启动代理：

```bash
langgraph dev
```

## 贡献指南

项目以 MIT 许可证开源，欢迎社区贡献！请随时提交 Pull Request 或创建 Issue 来讨论改进建议。




