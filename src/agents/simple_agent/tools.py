import uuid
from datetime import datetime

from langchain_core.tools import tool
from langchain_dev_utils.message_convert import format_sequence
from langgraph.prebuilt.tool_node import ToolRuntime

from src.agents.simple_agent.context import AssistantContext


@tool
def save_user_memory(content: str, runtime: ToolRuntime[AssistantContext]) -> str:
    """Save user long-term memory.

    Args:
        content: The memory content to save


    Returns:
        A string with success message
    """
    if not content or not content.strip():
        return "Error: Memory content cannot be empty."

    store = runtime.store
    if not store:
        return "Error: Memory store is not available."

    try:
        user_id = runtime.context.user_id
        memory_id = f"memory-{uuid.uuid4()}"
        timestamp = datetime.now().isoformat()

        store.put(
            (user_id, "memory"),
            memory_id,
            {
                "content": content,
                "user_name": runtime.context.user_name,
                "created_at": timestamp,
            },
            index=["content"],
        )

        content_preview = content[:100] + "..." if len(content) > 100 else content
        return f"Successfully saved user memory. Content: {content_preview}"
    except Exception as e:
        return f"Error saving memory: {str(e)}"


@tool
def get_user_memory(query: str, runtime: ToolRuntime[AssistantContext]) -> str:
    """Get user long-term memory by semantic search.

    Args:
        query: Search query to find relevant memories

    Returns:
        A string with user memory results or error message
    """
    if not query or not query.strip():
        return "Error: Search query cannot be empty."

    store = runtime.store
    if not store:
        return "Error: Memory store is not available."

    try:
        user_id = runtime.context.user_id
        items = store.search(
            (user_id, "memory"),
            query=query,
            limit=3,
        )

        if not items:
            return f"No user memory found for query: '{query}'"

        content = [item.value.get("content", "") for item in items]
        return "user_memory:\n" + format_sequence(content, with_num=True, separator="-")
    except Exception as e:
        return f"Error retrieving memory: {str(e)}"
