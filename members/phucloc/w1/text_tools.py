def word_count(text: str) -> dict[str, int]:
    normalized = text.lower()
    for punctuation in ".,!?;:":
        normalized = normalized.replace(punctuation, " ")

    counts: dict[str, int] = {}
    for word in normalized.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []

    ranked = sorted(word_count(text).items(), key=lambda item: (-item[1], item[0]))
    return ranked[:k]
