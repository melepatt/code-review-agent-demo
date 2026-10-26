"""Summary statistics for order values."""


def highest_order_or_zero(totals: list[float]) -> float:
    """Return the highest order value, or zero when no orders exist."""
    return max(totals)
