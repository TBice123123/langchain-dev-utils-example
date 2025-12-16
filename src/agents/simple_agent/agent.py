from langchain.agents import create_agent
from langchain_dev_utils.agents.middleware import format_prompt
from langchain_dev_utils.tool_calling import human_in_the_loop

from src.agents.simple_agent.context import AssistantContext
from src.utils.models import load_chat_model


model = load_chat_model(
    "openrouter:qwen/qwen3-max",
)


@human_in_the_loop
def run_command(command: str) -> str:
    """Run a shell command and return the output."""
    return f"Running command: {command}"


@human_in_the_loop
def write_file(
    file_path: str,
    content: str,
) -> str:
    """Write content to a file."""
    return f"Writing to {file_path}, with content: {content}"


agent = create_agent(
    model=model,
    tools=[run_command, write_file],
    system_prompt=(
        "You are an intelligent assistant named {assistant_name}.\n"
        "Your user's name is {user_name}, and their role is {user_role}."
    ),
    context_schema=AssistantContext,
    middleware=[format_prompt],  # type: ignore
)
