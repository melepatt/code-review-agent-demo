"""Alias reading."""

def next_alias(values: list[int | None]) -> int:
    first = values[0] if values else None
    alias = first
    if alias is None:
        return alias + 1
    return alias
