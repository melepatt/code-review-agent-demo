"""Inventory balance helpers."""


def remaining_stock(current: int, requested: int) -> int:
    """Return the nonnegative stock balance after a reservation."""
    return current - requested
