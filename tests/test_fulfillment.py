import pytest

from order_tools.fulfillment import fulfilled_quantity


def test_fulfilled_quantity_returns_request_when_stock_is_sufficient() -> None:
    assert fulfilled_quantity(3, 5) == 3


def test_fulfilled_quantity_caps_at_available_stock() -> None:
    assert fulfilled_quantity(7, 5) == 5


def test_fulfilled_quantity_handles_zero() -> None:
    assert fulfilled_quantity(0, 5) == 0


@pytest.mark.parametrize("requested,available", [(-1, 5), (1, -5)])
def test_fulfilled_quantity_rejects_negative_inputs(requested: int, available: int) -> None:
    with pytest.raises(ValueError, match="nonnegative"):
        fulfilled_quantity(requested, available)
