# Langchain-dev-utils Example Project

该仓库提供了一个示例项目，演示了如何利用 `langchain-dev-utils` 提供的工具函数，高效构建三种典型的智能体（agent）系统：

- **单智能体（Single Agent）**：适用于执行简单任务以及长期记忆存储相关的任务。
- **监督者-多智能体架构（Supervisor-Multi-Agent Architecture）**：通过一个中央监督者协调多个专业化智能体，适用于需要任务分解、规划和迭代优化的复杂场景。
- **交接架构（Handoffs Architecture）**：每个智能体负责特定任务，并在需要时将控制权转移给其他智能体。


<p align="center">
  <img src="./assets/image.png" alt="graph">
</p>


## 快速开始

1. 克隆本仓库：
```bash
git clone https://github.com/TBice123123/langchain-dev-utils-example.git  
cd langchain-dev-utils-example
```
2. 使用 uv 安装依赖：
```bash
uv sync
```
3. 创建.env文件
```bash
cp .env.example .env
```
4. 编辑 `.env` 文件，填入你的 API 密钥（需要 `ZhipuAI` 和 `Tavily` 的 API 密钥）。
   - 中国开发者需要使用`ZhipuAI`的此URL：`https://open.bigmodel.cn/api/paas/v4/`


5. 启动项目
```bash
langgraph dev
```

## 贡献指南

本项目采用 MIT 许可证开源。欢迎社区贡献！你可以提交 Pull Request，或创建 Issue 来讨论改进建议或想法。