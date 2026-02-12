from typing import Any, Optional, cast

from langchain.agents import create_agent
from langchain.tools import ToolRuntime
from langchain_core.messages import HumanMessage
from langchain_dev_utils.agents import wrap_agent_as_tool

from src.agents.supervisor.context import UserInput
from src.agents.supervisor.subagent.agent import (
    search_agent,
    vision_agent,
    weather_agent,
)
from src.utils.providers import load_chat_model


search_agent_tool = wrap_agent_as_tool(
    search_agent,
    "call_search_subagent",
    tool_description=(
        "Search the internet for current information, news, facts, or any online content. "
        "Use this tool when the user asks for information that requires internet access, "
        "such as latest news, current events, recent developments, or general web searches. "
        "Input: natural-language search query (e.g. 'search for the latest news on AI', "
        "'what is the current stock price of Apple', 'find information about quantum computing')"
    ),
)
weather_agent_tool = wrap_agent_as_tool(
    weather_agent,
    "call_weather_subagent",
    tool_description=(
        "Get current weather information for any city or location worldwide. "
        "Use this tool when the user asks about weather conditions, temperature, "
        "humidity, or any weather-related information for a specific place. "
        "Input: natural-language weather request specifying the city or location "
        "(e.g. 'weather in London', 'what's the temperature in Tokyo', "
        "'is it raining in New York')"
    ),
)


def prepare_image_messages(request: str, runtime: ToolRuntime) -> dict[str, Any] | str:
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
    return request


vision_agent_tool = wrap_agent_as_tool(
    vision_agent,
    "call_vision_subagent",
    tool_description=(
        "Handle ALL image-related tasks including describing images, analyzing visual content, "
        "understanding what's in an image, identifying objects, reading text from images, "
        "and any other visual analysis tasks. "
        "MUST use this tool whenever the user mentions images, uploads an image, "
        "asks for image description, or requests any visual analysis. "
        "Input: natural-language request describing what you want to know about the image "
        "(e.g. 'describe this image', 'what objects are in the picture', 'read the text in this image')"
    ),
    pre_input_hooks=prepare_image_messages,
)

SUPERVISOR_PROMPT = (
    "You are a helpful personal assistant. "
    "You have access to specialized sub-agents for different tasks:\n"
    "- Weather agent: Get current weather information for any city\n"
    "- Search agent: Search the internet for information\n"
    "- Vision agent: Handle ALL image-related tasks (describe, analyze, understand images)\n\n"
    "IMPORTANT RULES:\n"
    "1. For weather queries → use weather agent\n"
    "2. For internet searches → use search agent\n"
    "3. For ANY image-related request → MUST use vision agent\n"
    "4. For general questions without images → answer directly\n\n"
    "CRITICAL: You are a TEXT-ONLY model. You CANNOT see or process images. "
    "If the user mentions images, uploads an image, asks for image description, "
    "or requests ANY visual analysis, you MUST delegate to the vision agent. "
    "Do NOT attempt to handle image-related tasks yourself."
)

model = load_chat_model("zai:glm-5", thinking=True)

supervisor_agent = create_agent(
    model,
    tools=[search_agent_tool, weather_agent_tool, vision_agent_tool],
    system_prompt=SUPERVISOR_PROMPT,
    name="supervisor_agent",
    context_schema=UserInput,
)
