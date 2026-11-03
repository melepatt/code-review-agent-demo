from order_tools.metrics import order_total

def test_order_total_empty() -> None:
    assert order_total([]) == 0
