def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words in text."""
    return " ".join(reversed(text.split()))


def truncate(text: str, max_length: int) -> str:
    """Truncate text to max_length characters, appending '...' if truncated."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
