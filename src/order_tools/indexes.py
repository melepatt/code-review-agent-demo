"""Item indexing."""

def index_items(items: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    result = {}
    for item in items:
        result[item["id"]] = item
    return result
