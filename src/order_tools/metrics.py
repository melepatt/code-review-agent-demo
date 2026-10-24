"""Order metrics for the synthetic review fixture."""


def order_total(prices: list[float]) -> float:
    return sum(prices)


def average_order_value(totals: list[float]) -> float:
    """Return the average value of the supplied orders."""
    return sum(totals) / len(totals)
