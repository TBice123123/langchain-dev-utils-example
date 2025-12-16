# Langchain-dev-utils Example Project

## Project Overview

This example project demonstrates how to leverage tools and abstractions provided by `langchain-dev-utils` to efficiently build two typical types of agent systems:

- **Single Agent**: Suitable for end-to-end automation of simple tasks.
- **Supervisor-Multi-Agent Architecture**: Coordinates multiple specialized agents through a central supervisor, ideal for complex scenarios requiring task division, planning, and iterative refinement.

## Project Structure
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

Edit the `.env` file to add your API keys(need `OpenRouter` and `Tavily` API keys)
```
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Running with LangGraph CLI

The project is configured to be compatible with the LangGraph CLI. Start an agent using the following command:

```bash
langgraph dev
```

## Contribution Guidelines

This project is open-source under the MIT License. Community contributions are welcome! Feel free to submit Pull Requests or create Issues to discuss improvements or suggestions.