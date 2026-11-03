"""Report reading."""

def read_average(path: str, total: float, count: int) -> tuple[str, float]:
    data = open(path, encoding="utf-8").read()

    return data, total / count
