def count_lines(text: str) -> int:
    """Return the number of newline-separated lines in text.

    An empty string has 0 lines; a trailing newline does not add a line.
    """
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)
