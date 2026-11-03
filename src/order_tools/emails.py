"""Email normalization."""

def normalize_email(value: str) -> str:
    return value.strip().casefold()
