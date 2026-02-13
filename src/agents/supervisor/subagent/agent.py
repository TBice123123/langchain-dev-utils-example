from langchain.agents import create_agent

from src.agents.supervisor.subagent.tools import search_tool
from src.utils.providers import load_chat_model
from langchain.agents.middleware import ToolCallLimitMiddleware

model = load_chat_model("zai:glm-4.7-flash", thinking=False)

SEARCH_AGENT_PROMPT = (
    "You are a search assistant. "
    "IMPORTANT: Use the search_tool as few times as possible - ideally just once. "
    "Think carefully about your search query before calling the tool. "
    "Do not loop: after getting search results, analyze them and provide the answer directly. "
    "Only search again if the results are clearly irrelevant to the user's question."
)

search_agent = create_agent(
    model,
    tools=[search_tool],
    system_prompt=SEARCH_AGENT_PROMPT,
    name="search_agent",
    middleware=[ToolCallLimitMiddleware(tool_name="search_tool", thread_limit=3)],
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
