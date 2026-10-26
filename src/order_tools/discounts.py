"""Loyalty pricing helpers for orders."""


def loyalty_price(subtotal: float, years: int) -> float:
    """Apply ten percent off for customers with five or more years."""
    if years > 5:
        return subtotal * 0.9
    return subtotal
