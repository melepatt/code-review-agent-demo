def tax_percent(region: str) -> int:
    return {"north": 7, "south": 5}.get(region, 0)
