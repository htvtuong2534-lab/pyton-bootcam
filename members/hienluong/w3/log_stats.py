from collections import Counter
from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict:
    if not pairs:
        return {
            "counts": {},
            "p95": {},
            "slowest": None,
        }

    counts = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency_ms)

    p95 = {}

    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=p95.get)

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }