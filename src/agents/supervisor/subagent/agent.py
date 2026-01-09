from langchain.agents import create_agent

from src.agents.supervisor.subagent.tools import get_current_weather, search_tool
from src.utils.providers import load_chat_model

model = load_chat_model("zai:glm-4.5", thinking=False)


WEATHER_AGENT_PROMPT = (
    "You are a weather assistant. "
    "Accurately parse weather requests in natural language (e.g., 'London weather'), extract and standardize the city name, then call get_current_weather to obtain real-time weather. "
    "Regardless of whether the user specifies units, the final response should always include temperature, weather conditions, etc."
)

weather_agent = create_agent(
    model,
    tools=[get_current_weather],
    system_prompt=WEATHER_AGENT_PROMPT,
    name="weather_agent",
)

SEARCH_AGENT_PROMPT = (
    "You are a search assistant. "
    "Compose professional search queries based on natural-language requests. "
    "Extract search keywords and parameters. "
    "Use tavily_search to find relevant information. "
    "Always confirm in your final response what has been searched."
)

search_agent = create_agent(
    model,
    tools=[search_tool],
    system_prompt=SEARCH_AGENT_PROMPT,
    name="search_agent",
)


VISION_AGENT_PROMPT = (
    "You are a vision assistant. "
    "Analyze and understand visual content from images. "
    "Provide detailed and accurate descriptions of what you see in the image. "
    "Answer questions based on the visual information. "
    "Focus on key elements, objects, scenes, text, and any relevant details. "
    "Be specific and comprehensive in your visual analysis."
)

vision_model = load_chat_model("zai:glm-4.6v")
vision_agent = create_agent(
    vision_model,
    system_prompt=VISION_AGENT_PROMPT,
    name="vision_agent",
)
