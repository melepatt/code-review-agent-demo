from decimal import Decimal
from order_tools.rounding import round_amount

def test_round_amount() -> None:
    assert round_amount(Decimal("1.235")) == Decimal("1.24")
