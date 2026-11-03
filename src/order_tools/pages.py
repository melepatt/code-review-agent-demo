"""Page helpers."""

def page_items(items: list[str], page_size: int) -> list[str]:
    if page_size <= 0:
        return []
    return items[: page_size - 1]
