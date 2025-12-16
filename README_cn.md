# LangChain 开发工具示例项目

## 项目概述

本示例项目演示了如何利用 `langchain-dev-utils` 提供的工具与抽象，高效构建两类典型智能体系统：
- **单智能体（Simple Agent）**：适用于端到端的简单任务自动化。
- **主管-多智能体架构（Supervisor-Multi-Agent）**：通过一个主管协调多个专业智能体，适用于需分工、规划与迭代的复杂场景。

## 项目结构

```
langchain-dev-utils-example/
├── lib/                          # 库模块
│   ├── __init__.py               # 库初始化
│   ├── models.py                 # 模型定义和工具
│   └── register.py               # 模型提供商注册
├── src/                          # 源代码
│   └── agents/                   # 代理实现
│       ├── __init__.py           # 代理模块初始化
│       ├── simple_agent/         # 简单智能体示例
│       │   ├── __init__.py       # 简单代理模块初始化
│       │   ├── agent.py          # 简单代理定义
│       │   └── context.py        # 上下文模式定义
│       └── supervisor/           # 主管多智能体架构
│           ├── __init__.py       # 主管模块初始化
│           ├── supervisor.py     # 主管智能体
│           └── subagent.py       # 专业化子智能体
├── .env.example                  # 环境变量模板
├── .gitignore                    # Git 忽略文件
├── .python-version               # Python 版本规范
├── LICENSE                       # MIT 许可证
├── README.md                     # 英文版说明文件
├── README_cn.md                  # 中文版说明文件
├── langgraph.json               # LangGraph 配置
├── pyproject.toml               # 项目依赖
└── uv.lock                      # 依赖锁定文件
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

编辑 `.env` 文件，添加您的 API 密钥：
```
OPENROUTER_API_KEY=your_openrouter_api_key
```

## 使用方法

### 通过 LangGraph CLI 运行代理

项目已配置为与 LangGraph CLI 兼容。使用以下命令启动代理：

```bash
langgraph dev
```

## 贡献指南

项目以 MIT 许可证开源，欢迎社区贡献！请随时提交 Pull Request 或创建 Issue 来讨论改进建议。




