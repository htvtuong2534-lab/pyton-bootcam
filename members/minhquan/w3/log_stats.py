import math
from collections import Counter, defaultdict


def calculate_p95(latencies: list[float]) -> float:
    sorted_latencies = sorted(latencies)
    n = len(sorted_latencies)
    index = math.ceil(0.95 * n) - 1
    index = max(0, min(index, n - 1))
    return float(sorted_latencies[index])


def analyse(pairs: list[tuple[str, float]]) -> dict:
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts = Counter()
    latencies_by_route = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)

    p95_by_route = {}
    for route, latencies in latencies_by_route.items():
        p95_by_route[route] = calculate_p95(latencies)

    slowest_route = max(p95_by_route, key=p95_by_route.get)

    return {"counts": counts, "p95": p95_by_route, "slowest": slowest_route}