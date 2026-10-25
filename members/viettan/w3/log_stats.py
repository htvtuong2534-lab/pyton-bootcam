from collections import Counter, defaultdict
from math import ceil
from typing import Iterable


def analyse(pairs: Iterable[tuple[str, float]]) -> dict:
    """Analyse request counts and p95 latency for each route."""
    latencies = defaultdict(list)

    for route, latency in pairs:
        latencies[route].append(float(latency))

    counts = Counter()
    p95_by_route = {}

    for route, values in latencies.items():
        counts[route] = len(values)
        sorted_values = sorted(values)
        index = max(0, ceil(0.95 * len(sorted_values)) - 1)
        p95_by_route[route] = sorted_values[index]

    highest_p95_route = (
        max(p95_by_route, key=p95_by_route.get)
        if p95_by_route
        else None
    )

    return {
        "counts": dict(counts),
        "p95": p95_by_route,
        "highest_p95_route": highest_p95_route,
    }
