def word_count(text: str) -> dict[str, int]:
    words = text.lower().split()
    result = {}

    for word in words:
        word = word.strip(".,!?:;")
        if word:
            result[word] = result.get(word, 0) + 1

    return result


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    result = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return result[:k]