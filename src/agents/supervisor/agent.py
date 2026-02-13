from typing import Any, Optional, cast

from langchain.agents import create_agent
from langchain.tools import ToolRuntime
from langchain_core.messages import HumanMessage
from langchain_dev_utils.agents import wrap_all_agents_as_tool
from langchain_dev_utils.agents.wrap import get_subagent_name

from src.agents.supervisor.context import UserInput
from src.agents.supervisor.subagent.agent import search_agent, vision_agent
from src.utils.providers import load_chat_model


def prepare_message(request: str, runtime: ToolRuntime) -> dict[str, Any] | str:
    subagent_name = get_subagent_name(runtime)
    if subagent_name == "vision_agent":
        context = cast(Optional[UserInput], runtime.context)
        if context:
            image_url = context.image_url
            if image_url:
                return {
                    "messages": [
                        HumanMessage(
                            content_blocks=[
                                {
                                    "type": "image",
                                    "url": image_url,
                                },
                                {
                                    "type": "text",
                                    "text": request,
                                },
                            ]
                        )
                    ]
                }
    elif subagent_name == "search_agent":
        import datetime

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Current time: {current_time}\n\nUser request: {request}"
    return request


task = wrap_all_agents_as_tool(
    [search_agent, vision_agent],
    tool_description=(
        "Call a subagent to handle specific tasks. "
        "Available subagents:\n"
        "- search_agent: Search the internet for information, news, facts, or any online content\n"
        "- vision_agent: Handle ALL image-related tasks including describing, analyzing, understanding images\n\n"
        "Input must include 'agent_name' parameter to specify which subagent to call:\n"
        "- agent_name='search_agent' for internet searches\n"
        "- agent_name='vision_agent' for any image-related tasks"
    ),
    pre_input_hooks=prepare_message,
)


SUPERVISOR_PROMPT = (
    "You are a helpful personal assistant. "
    "You have access to specialized sub-agents for different tasks:\n"
    "- Search agent: Search the internet for information\n"
    "- Vision agent: Handle ALL image-related tasks (describe, analyze, understand images)\n\n"
    "IMPORTANT RULES:\n"
    "1. For internet searches → use task tool with agent_name='search_agent'\n"
    "2. For ANY image-related request → MUST use task tool with agent_name='vision_agent'\n"
    "   - This includes: describing images, analyzing images, understanding images, "
    "     reading text from images, identifying objects, visual analysis\n"
    "   - EVEN IF the user mentions 'image' or 'picture' but didn't upload one, "
    "     you MUST still call the vision agent to handle the request\n"
    "3. For general questions without images → answer directly\n\n"
    "CRITICAL: You are a TEXT-ONLY model. You CANNOT see or process images. "
    "If the user mentions images, pictures, or any visual content, "
    "you MUST delegate to the vision agent using the task tool with agent_name='vision_agent'. "
    "Do NOT attempt to handle image-related tasks yourself."
)


model = load_chat_model("zai:glm-5", thinking=True)

supervisor_agent = create_agent(
    model,
    tools=[task],
    system_prompt=SUPERVISOR_PROMPT,
    name="supervisor_agent",
    context_schema=UserInput,
)
