"""Retry scheduling helpers."""


def retry_delay(attempt: int) -> int:
    """Return a capped exponential delay for a zero-based attempt."""
    if attempt < 0:
        raise ValueError("attempt must be nonnegative")
    return min(2**attempt, 60)
