def summary(scores: list[float]) -> dict:
    """Calculate the minimum, maximum, mean and median of scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    n = len(ordered)

    mean = sum(ordered) / n

    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

    return {
        "min": min(ordered),
        "max": max(ordered),
        "mean": round(mean, 2),
        "median": round(median, 2),
    }


if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))