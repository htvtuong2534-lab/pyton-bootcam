
def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    n = len(ordered)

    minimum = min(ordered)
    maximum = max(ordered)
    mean = round(sum(ordered) / n, 2)

    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

    median = round(median, 2)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median
    }