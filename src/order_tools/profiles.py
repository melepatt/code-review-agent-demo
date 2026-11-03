"""Profile labels."""

def display_name(profile: dict[str, str]) -> str:
    name = profile.get("name")
    return name.strip()
