import re


def slugify(text: str) -> str:
    """Return a lowercase slug of text containing only [a-z0-9-].

    Spaces become '-', other disallowed characters are removed, runs of '-'
    are collapsed into one, and leading/trailing '-' are stripped.
    """
    slug = text.strip().lower().replace(" ", "-")
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")
