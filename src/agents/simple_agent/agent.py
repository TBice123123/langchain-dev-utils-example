from langchain.agents import create_agent
from langchain_dev_utils.agents.middleware import format_prompt

from src.agents.simple_agent.context import AssistantContext
from src.agents.simple_agent.tools import save_user_memory
from src.agents.simple_agent.tools import get_user_memory
from src.utils.providers import load_chat_model

model = load_chat_model(
    "zai:glm-4.7",
    thinking=True,
    reasoning_keep_policy="current",
)


agent = create_agent(
    model=model,
    tools=[save_user_memory, get_user_memory],
    system_prompt=(
        "You are an intelligent assistant named {assistant_name}.\n"
        "Your user's name is {user_name}, and their role is {user_role}."
    ),
    context_schema=AssistantContext,
    middleware=[format_prompt],  # type: ignore
)
