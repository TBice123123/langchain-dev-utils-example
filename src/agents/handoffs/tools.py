from typing import Annotated
from langchain_core.tools import tool
from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    product_name: str
    quantity: int
    price: int
    status: str
    created_at: str
    address: str = ""
    tracking_no: str = ""


ORDERS: dict[str, Order] = {
    "ORD-20250115-A1B2": Order(
        order_id="ORD-20250115-A1B2",
        product_name="Wireless Earbuds",
        quantity=1,
        price=299,
        status="shipped",
        created_at="2025-01-15 10:30:00",
        address="Beijing, Chaoyang District",
        tracking_no="SF1234567890",
    ),
    "ORD-20250120-C3D4": Order(
        order_id="ORD-20250120-C3D4",
        product_name="Mechanical Keyboard",
        quantity=1,
        price=599,
        status="pending",
        created_at="2025-01-20 14:22:00",
        address="Shanghai, Pudong District",
    ),
    "ORD-20250122-E5F6": Order(
        order_id="ORD-20250122-E5F6",
        product_name="Wireless Mouse",
        quantity=2,
        price=198,
        status="delivered",
        created_at="2025-01-22 09:15:00",
        address="Shenzhen, Nanshan District",
        tracking_no="YT9876543210",
    ),
}


REFUNDS: dict[str, dict] = {
    "RFD-20250118-X7Y8": {
        "refund_id": "RFD-20250118-X7Y8",
        "order_id": "ORD-20250115-A1B2",
        "status": "completed",
        "reason": "Product quality issue",
        "amount": 299,
        "created_at": "2025-01-18 16:00:00",
    },
}


PRODUCTS = [
    {"product_id": "P-001", "name": "Wireless Earbuds", "price": 299, "stock": 50},
    {"product_id": "P-002", "name": "Mechanical Keyboard", "price": 599, "stock": 20},
    {"product_id": "P-003", "name": "Wireless Mouse", "price": 99, "stock": 100},
]


@tool
def list_orders() -> str:
    """Query user's order list."""
    if not ORDERS:
        return "No orders found."
    result = []
    for order in ORDERS.values():
        result.append(
            f"- {order.order_id}: {order.product_name} x{order.quantity}, "
            f"Status: {order.status}, Created: {order.created_at}"
        )
    return "Your orders:\n" + "\n".join(result)


@tool
def get_order_detail(order_id: Annotated[str, "Order ID to query"]) -> str:
    """Query order details including status, receiver, items."""
    order = ORDERS.get(order_id)
    if not order:
        return f"Order {order_id} not found"
    return (
        f"Order ID: {order.order_id}\n"
        f"Product: {order.product_name} x{order.quantity}\n"
        f"Price: ¥{order.price}\n"
        f"Status: {order.status}\n"
        f"Address: {order.address}\n"
        f"Tracking: {order.tracking_no or 'N/A'}\n"
        f"Created: {order.created_at}"
    )


@tool
def refund_policy() -> str:
    """View refund policy."""
    return (
        "Refund Policy:\n"
        "- 7-day return window\n"
        "- Requirements: Product intact, accessories complete, order number provided\n"
        "- Notes: Some promotional items not eligible for refund, "
        "refund time varies by payment method"
    )


@tool
def get_refund_status(refund_id: Annotated[str, "Refund ID to query"]) -> str:
    """Query refund status."""
    refund = REFUNDS.get(refund_id)
    if not refund:
        return "Refund not found."
    return (
        f"Refund ID: {refund['refund_id']}\n"
        f"Order ID: {refund['order_id']}\n"
        f"Status: {refund['status']}\n"
        f"Amount: ¥{refund['amount']}\n"
        f"Reason: {refund['reason']}\n"
        f"Created: {refund['created_at']}"
    )


@tool
def list_products() -> str:
    """List all available products."""
    return "\n".join(
        f"- {p['name']}: ¥{p['price']}, Stock: {p['stock']}" for p in PRODUCTS
    )


@tool
def get_product(product_id: Annotated[str, "Product ID"]) -> str:
    """Get product details by ID."""
    for p in PRODUCTS:
        if p["product_id"] == product_id:
            return f"Product: {p['name']}, Price: ¥{p['price']}, Stock: {p['stock']}"
    return "Product not found"
