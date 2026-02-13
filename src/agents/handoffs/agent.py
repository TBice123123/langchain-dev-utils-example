from langchain.agents import create_agent
from langchain_dev_utils.agents.middleware import HandoffAgentMiddleware
from langchain_dev_utils.agents.middleware.handoffs import AgentConfig

from src.agents.handoffs.tools import (
    list_orders,
    get_order_detail,
    refund_policy,
    get_refund_status,
    list_products,
    get_product,
)
from src.utils.providers import load_chat_model


model = load_chat_model("zai:glm-5", thinking=False)

ORDER_AGENT_PROMPT = (
    "You are an order assistant. Use tools to:\n"
    "- list_orders: Query order list\n"
    "- get_order_detail: Query order details\n"
    "Use tools first, then answer based on results."
)

REFUND_AGENT_PROMPT = (
    "You are a refund assistant. Use tools to:\n"
    "- get_refund_status: Query refund status\n"
    "- refund_policy: View refund policy\n"
    "Use tools first, then answer based on results."
)

PRODUCT_AGENT_PROMPT = (
    "You are a product assistant. Use tools to:\n"
    "- list_products: List all products\n"
    "- get_product: Get product details by ID\n"
    "Use tools first, then answer based on results."
)

general_prompt = (
    "You are a general assistant. Handle various questions:\n"
    "- Order queries → transfer to order_agent\n"
    "- Refund questions → transfer to refund_agent\n"
    "- Product info → transfer to product_agent"
)

agents_config: dict[str, AgentConfig] = {
    "order_agent": {
        "prompt": ORDER_AGENT_PROMPT,
        "tools": [list_orders, get_order_detail],
        "handoffs": "all",
    },
    "refund_agent": {
        "prompt": REFUND_AGENT_PROMPT,
        "tools": [get_refund_status, refund_policy],
        "handoffs": "all",
    },
    "product_agent": {
        "prompt": PRODUCT_AGENT_PROMPT,
        "tools": [list_products, get_product],
        "handoffs": "all",
    },
    "general_agent": {
        "prompt": general_prompt,
        "default": True,
        "handoffs": "all",
    },
}

agent = create_agent(
    model=model,
    middleware=[
        HandoffAgentMiddleware(
            agents_config=agents_config,
            custom_handoffs_tool_descriptions={
                "order_agent": "Transfer to order assistant for order queries",
                "refund_agent": "Transfer to refund assistant for refund queries",
                "product_agent": "Transfer to product assistant for product info",
                "general_agent": "Transfer to general assistant for other questions",
            },
        )
    ],
)
