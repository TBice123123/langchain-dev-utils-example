from typing import Annotated
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import warnings

warnings.filterwarnings("ignore")


@tool
def search_tool(
    query: Annotated[
        str, "The search query. Use clear keywords instead of full sentences."
    ],
) -> str:
    """A search engine for finding current information, news, and web content."""
    search_tool = TavilySearch()
    return search_tool.invoke({"query": query})
