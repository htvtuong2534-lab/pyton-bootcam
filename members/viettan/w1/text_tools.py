
def word_count(text: str) -> dict[str, int]:
    """Count words without case sensitivity and ignore common punctuation."""
    punctuation = ".,!?;:"
    cleaned = text.lower().translate(
        str.maketrans("", "", punctuation)
    )

    counts = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, sorted by count then alphabetically."""
    if k <= 0:
        return []

    counts = word_count(text)
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


if __name__ == "__main__":
    text = "Git is fun. Git is fast!"
    print(word_count(text))
    print(top_k(text, 2))   