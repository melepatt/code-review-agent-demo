from .rates import tax_percent

def total_with_tax(subtotal: float, region: str) -> float:
    return subtotal + subtotal * tax_percent(region)
