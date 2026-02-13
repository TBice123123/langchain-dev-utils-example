# AGENTS.md - Development Guidelines for Agents

This document provides guidelines for agents operating in this repository.

## Project Overview

This is a LangChain-based agent project with multiple agent architectures:
- Single Agent (simple_agent)
- Supervisor-Multi-Agent (supervisor)
- Handoffs Architecture (handoffs)

Python >= 3.11 is required.

## Commands

### Installation
```bash
# Install dependencies
uv sync

# Install dev dependencies
uv sync --group dev
```

### Running the Project
```bash
# Start LangGraph dev server
langgraph dev
```

### Linting
```bash
# Run ruff linter
ruff check .

# Run ruff with auto-fix
ruff check --fix .
```

### Type Checking
This project uses type annotations. Ensure your code is type-safe.

## Code Style Guidelines

### Imports

**Order (top to bottom):**
1. Standard library imports (`uuid`, `datetime`, `typing`, etc.)
2. Third-party imports (`langchain`, `langchain_core`, etc.)
3. Local/application imports (`from src...`)

**Example:**
```python
import uuid
from datetime import datetime
from typing import Annotated, Optional

from langchain.agents import create_agent
from langchain_core.tools import tool

from src.agents.simple_agent.context import AssistantContext
from src.agents.simple_agent.tools import save_user_memory
from src.utils.providers import load_chat_model
```

**Rules:**
- Use absolute imports (e.g., `from src.agents...` not `from ..agents...`)
- Separate import groups with one blank line
- Do NOT use `# noqa` comments unless absolutely necessary
- Sort imports alphabetically within each group

### Formatting

- Maximum line length: 100 characters (follows ruff default)
- Use 4 spaces for indentation (no tabs)
- Use blank lines sparingly to separate logical sections
- Remove trailing whitespace

### Type Annotations

**Required for:**
- Function parameters and return types
- Class attributes
- TypedDict definitions

**Use `Annotated` for tool arguments:**
```python
from typing import Annotated
from langchain_core.tools import tool

@tool
def my_tool(query: Annotated[str, "Description of the query"]) -> str:
    """Tool description."""
    return "result"
```

**Use TypedDict for context/state schemas:**
```python
from typing import TypedDict

class UserContext(TypedDict):
    user_id: str
    user_name: str
```

### Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Files | snake_case | `my_agent.py`, `tools.py` |
| Functions | snake_case | `create_agent()`, `load_chat_model()` |
| Classes | PascalCase | `class AssistantContext:`, `class Order:` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRY = 3` |
| Tools | snake_case | `save_user_memory`, `get_order_detail` |
| Agent names | snake_case | `"order_agent"`, `"general_agent"` |

### Tool Definition

**Always use `@tool` decorator from `langchain_core.tools`:**
```python
from typing import Annotated
from langchain_core.tools import tool

@tool
def my_tool(
    param: Annotated[str, "Description of parameter"],
) -> str:
    """Tool description shown to the LLM."""
    return "result"
```

**Rules:**
- Always provide descriptions for tool parameters using `Annotated`
- Keep tool docstrings concise but informative
- Return string results from tools
- Handle errors gracefully and return error messages as strings

### Error Handling

**For tools:** Return error messages as strings instead of raising exceptions:
```python
@tool
def my_tool(param: str) -> str:
    try:
        # operation that might fail
        return "Success result"
    except Exception as e:
        return f"Error: {str(e)}"
```

**For agents:** Let the framework handle exceptions; focus on clean, readable code.

### Agent Creation

**Using `create_agent`:**
```python
from langchain.agents import create_agent
from src.utils.providers import load_chat_model

model = load_chat_model("zai:glm-4.7-flash", thinking=False)

agent = create_agent(
    model=model,
    tools=[my_tool],
    system_prompt="Your system prompt here.",
    name="agent_name",
)
```

**Using HandoffAgentMiddleware:**
```python
from langchain.agents import create_agent
from langchain_dev_utils.agents.middleware import HandoffAgentMiddleware
from langchain_dev_utils.agents.middleware.handoffs import AgentConfig

agents_config: dict[str, AgentConfig] = {
    "agent_a": {
        "prompt": "System prompt for agent A",
        "tools": [tool_a, tool_b],
        "handoffs": ["agent_b", "default_agent"],
    },
    "default_agent": {
        "prompt": "Default agent prompt",
        "default": True,  # Only one agent can be default
        "handoffs": "all",  # Can handover to all other agents
    },
}

agent = create_agent(
    model=model,
    middleware=[HandoffAgentMiddleware(agents_config=agents_config)],
)
```

### Context Schemas

Define context using TypedDict:
```python
from typing import TypedDict

class AssistantContext(TypedDict):
    user_id: str
    user_name: str
    user_role: Optional[str]
    image_url: Optional[str]
```

### General Best Practices

1. **Keep tools focused:** Each tool should do one thing well
2. **Use descriptive names:** Agent and tool names should clearly indicate purpose
3. **Prefer explicit over implicit:** Be explicit with types and parameters
4. **Document complex logic:** Add docstrings for non-trivial functions
5. **Test your agents:** Verify agent behavior with various inputs
6. **Handle edge cases:** Consider empty inputs, missing data, etc.

### File Structure

```
src/
├── agents/
│   ├── simple_agent/     # Single agent with memory
│   ├── supervisor/       # Supervisor + sub-agents
│   │   └── subagent/     # Sub-agents
│   └── handoffs/         # Handoffs architecture
└── utils/
    └── providers/        # Model providers
```

### Before Submitting Code

1. Run `ruff check .` to catch linting issues
2. Ensure all imports are correct and sorted
3. Check type annotations are present and correct
4. Verify agent/tool names are consistent
5. Test the functionality works as expected
