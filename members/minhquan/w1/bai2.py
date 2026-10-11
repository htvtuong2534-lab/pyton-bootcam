from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words, ignoring specified punctuation."""
    punctuation = ".,!?;:"
    cleaned = text.lower().translate(str.maketrans("", "", punctuation))
    return dict(Counter(cleaned.split()))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, breaking ties alphabetically."""
    if k <= 0:
        return []
    return sorted(word_count(text).items(), key=lambda item: (-item[1], item[0]))[:k]
