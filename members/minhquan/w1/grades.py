def summary(scores: list[float]) -> dict:
    """Return min, max, mean, and median of scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    n = len(ordered)
    median = ordered[n // 2] if n % 2 else (ordered[n // 2 - 1] + ordered[n // 2]) / 2

    return {
        "min": min(ordered),
        "max": max(ordered),
        "mean": round(sum(ordered) / n, 2),
        "median": round(median, 2),
    }
