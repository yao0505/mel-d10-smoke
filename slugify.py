def slugify(text: str) -> str:
    """Return text stripped, lowercased, with spaces replaced by '-'."""
    return text.strip().lower().replace(" ", "-")
