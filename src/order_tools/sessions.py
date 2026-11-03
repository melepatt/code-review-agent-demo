"""Session values."""

def session_value(user_id: str) -> str:
    return user_id[::-1]
