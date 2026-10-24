from order_tools.metrics import order_total


def test_order_total_sums_prices() -> None:
    assert order_total([10.0, 5.5]) == 15.5
