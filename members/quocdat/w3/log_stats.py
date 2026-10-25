from collections import Counter
from math import ceil
from typing import Iterable, Hashable


def _percentile_95(values: list[int]) -> int:
    if not values:
        raise ValueError("No latency values available")

    ordered = sorted(values)
    index = max(1, ceil(0.95 * len(ordered))) - 1
    return ordered[index]


def analyse(pairs: Iterable[tuple[str, int]]) -> dict[str, object]:
    counts: Counter[str] = Counter()
    latencies_by_route: dict[str, list[int]] = {}

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies_by_route.setdefault(route, []).append(latency_ms)

    p95 = {
        route: _percentile_95(latencies)
        for route, latencies in sorted(latencies_by_route.items())
    }

    slowest = None
    if p95:
        slowest = max(p95, key=p95.get)

    return {"counts": counts, "p95": p95, "slowest": slowest}
