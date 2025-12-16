# LangChain Development Tools Example Project

## Project Overview

This example project demonstrates how to leverage tools and abstractions provided by `langchain-dev-utils` to efficiently build two typical types of agent systems:

- **Single Agent**: Suitable for end-to-end automation of simple tasks.
- **Supervisor-Multi-Agent Architecture**: Coordinates multiple specialized agents through a central supervisor, ideal for complex scenarios requiring task division, planning, and iterative refinement.

## Project Structure

```
langchain-dev-utils-example/
├── lib/                          # Library modules
│   ├── __init__.py               # Library initialization
│   ├── models.py                 # Model definitions and utilities
│   └── register.py               # Model provider registration
├── src/                          # Source code
│   └── agents/                   # Agent implementations
│       ├── __init__.py           # Agents module initialization
│       ├── simple_agent/         # Simple agent example
│       │   ├── __init__.py       # Simple agent module initialization
│       │   ├── agent.py          # Simple agent definition
│       │   └── context.py        # Context schema definition
│       └── supervisor/           # Supervisor-multi-agent architecture
│           ├── __init__.py       # Supervisor module initialization
│           ├── supervisor.py     # Supervisor agent
│           └── subagent.py       # Specialized sub-agents
├── .env.example                  # Environment variable template
├── .gitignore                    # Git ignore file
├── .python-version               # Python version specification
├── LICENSE                       # MIT License
├── README.md                     # This file
├── README_cn.md                  # Chinese version of README
├── langgraph.json               # LangGraph configuration
├── pyproject.toml               # Project dependencies
└── uv.lock                      # Dependency lock file
```

## Installation Steps

1. Clone this repository:
```bash
git clone https://github.com/TBice123123/langchain-dev-utils-example.git
cd langchain-dev-utils-example
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Configure environment variables:
```bash
cp .env.example .env
```

Edit the `.env` file to add your API keys:
```
OPENROUTER_API_KEY=your_openrouter_api_key
```

## Usage

### Running Agents via LangGraph CLI

The project is configured to be compatible with the LangGraph CLI. Start an agent using the following command:

```bash
langgraph dev
```

## Contribution Guidelines

This project is open-source under the MIT License. Community contributions are welcome! Feel free to submit Pull Requests or create Issues to discuss improvements or suggestions.