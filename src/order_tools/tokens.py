"""Account token helpers."""


def reset_token(user_id: str) -> str:
    """Return a token for an account recovery request."""
    return f"{user_id}-reset"
