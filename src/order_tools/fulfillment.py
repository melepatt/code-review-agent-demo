"""Order fulfillment helpers."""


def fulfilled_quantity(requested: int, available: int) -> int:
    """Return the fulfillable quantity after validating both inputs."""
    if requested < 0 or available < 0:
        raise ValueError("quantities must be nonnegative")
    return min(requested, available)
