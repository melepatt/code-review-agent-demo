"""Access fallback."""

def can_edit(roles: set[str] | None) -> bool:
    if not roles:
        return False
    return "editor" in roles
