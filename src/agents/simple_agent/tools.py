import uuid

from langchain_core.tools import tool
from langchain_dev_utils.message_convert import format_sequence
from langgraph.prebuilt.tool_node import ToolRuntime

from src.agents.simple_agent.context import AssistantContext


@tool
def save_user_memory(content: str, runtime: ToolRuntime[AssistantContext]) -> str:
    """Save user long-term memory."""

    store = runtime.store
    user_id = runtime.context.user_id
    if store:
        store.put(
            ("user", user_id),
            f"memory-{str(uuid.uuid4())}",
            {"content": content, "user_name": runtime.context.user_name},
            index=["content"],
        )
    return "Successfully saved user memory."


@tool
def get_user_memory(query: str, runtime: ToolRuntime[AssistantContext]) -> str:
    """Get user long-term memory."""
    store = runtime.store
    user_id = runtime.context.user_id
    if store:
        items = store.search(
            ("user", user_id),
            query=query,
            limit=3,
        )

        content = [item.value.get("content", "") for item in items]
        if items:
            return (
                "user_memory:"
                + "\n"
                + format_sequence(content, with_num=True, separator="-")
            )

    return "No user memory found."
