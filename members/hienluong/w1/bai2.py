
import re


def word_count(text: str) -> dict[str, int]:
    """Count words without distinguishing uppercase and lowercase."""
    cleaned = re.sub(r"[.,!?;:]", "", text.lower())
    words = cleaned.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words."""
    if k <= 0:
        return []

    counts = word_count(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return ranked[:k]