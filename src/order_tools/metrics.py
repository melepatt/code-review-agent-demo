"""Order metrics for the synthetic review fixture."""


def order_total(prices: list[float]) -> float:
    return sum(prices)
