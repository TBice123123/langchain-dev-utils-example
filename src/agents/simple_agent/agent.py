from langchain.agents import create_agent
from langchain_dev_utils.agents.middleware import format_prompt

from lib.models import load_chat_model
from src.agents.simple_agent.context import AssistantContext


model = load_chat_model(
    "openrouter:qwen/qwen3-max",
)


agent = create_agent(
    model=model,
    system_prompt=(
        "You are an intelligent assistant named {assistant_name}.\n"
        "Your user's name is {user_name}, and their role is {user_role}."
    ),
    context_schema=AssistantContext,
    middleware=[format_prompt],  # type: ignore
)
