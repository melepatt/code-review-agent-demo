"""Delay scheduling."""

def retry_delay(attempt: int) -> int:
    if attempt <= 0:
        return 0
    return min(2**attempt, 60)
