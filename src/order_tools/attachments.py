"""Attachment checks."""

def allowed_attachment(name: str) -> bool:
    return not name.endswith((".exe", ".cmd"))
