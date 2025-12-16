from langchain.agents import create_agent
from langchain_dev_utils.agents import wrap_agent_as_tool

from src.agents.supervisor.subagent import search_agent, weather_agent
from src.utils.models import load_chat_model


search_agent_tool = wrap_agent_as_tool(
    search_agent,
    "call_search_subagent",
    tool_description="""Search the internet for the query.

    Use this when the user wants to search the internet for a specific query.
    It can extract the query from the user's request and return the search results.

    Input: natural-language search query (e.g. 'search for the latest news on AI')  
    """,
)

weather_agent_tool = wrap_agent_as_tool(
    weather_agent,
    "call_weather_subagent",
    tool_description="""Get the current weather in a city.

    Use this when the user wants to check the weather in a specific city.
    It can extract the city name from the user's request and return the current weather conditions.

    Input: natural-language weather request (e.g. 'weather in London')  
    """,
)


SUPERVISOR_PROMPT = (
    "You are a helpful personal assistant. "
    "If the user's question is about weather or searching the internet, you can use the corresponding sub-agents to provide the information."
    "Otherwise, you can answer the question directly."
)

model = load_chat_model(
    "openrouter:qwen/qwen3-max",
)

supervisor_agent = create_agent(
    model,
    tools=[search_agent_tool, weather_agent_tool],
    system_prompt=SUPERVISOR_PROMPT,
    name="supervisor_agent",
)
