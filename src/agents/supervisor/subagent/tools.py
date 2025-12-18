from langchain_core.tools import tool
from langchain_tavily import TavilySearch


search_tool = TavilySearch(max_results=2)


@tool
def get_current_weather(city: str) -> str:
    """Get the current weather in a city."""
    return f"In {city}, 20°C, Clear sky"
