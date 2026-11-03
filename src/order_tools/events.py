"""Event labels for application logs."""

def event_label(order_id: str) -> str:
    return f"order:{order_id}"
