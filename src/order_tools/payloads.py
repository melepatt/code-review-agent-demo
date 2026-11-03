"""Payload reading."""

def first_item(payload: dict[str, list[str]]) -> str | None:
    return payload["items"][0] if payload["items"] else None
