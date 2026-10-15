def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    mean = sum(sorted_scores) / n

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": sorted_scores[0],
        "max": sorted_scores[-1],
        "mean": round(mean, 2),
        "median": round(median, 2),
    }

