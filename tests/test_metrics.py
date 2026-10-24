from order_tools.metrics import order_count, order_total


def test_order_total_sums_prices() -> None:
    assert order_total([10.0, 5.5]) == 15.5


def test_order_count_counts_nonempty_prices() -> None:
    assert order_count([10.0, 5.5]) == 2


def test_order_count_handles_empty_prices() -> None:
    assert order_count([]) == 0
