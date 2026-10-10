"""W1-1: summarise a non-empty list of grades."""


def summary(scores: list[float]) -> dict[str, float]:
    """Return minimum, maximum, mean and median without changing scores.

    Mean and median are rounded to two decimal places. Empty input raises
    ValueError because it has no minimum, maximum or median.
    """
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    count = len(ordered)
    middle = count // 2
    if count % 2:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(scores) / count, 2),
        "median": round(median, 2),
    }
