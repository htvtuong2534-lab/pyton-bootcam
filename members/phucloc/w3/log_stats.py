from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil, isfinite


def analyse(pairs: Iterable[tuple[str, float]]) -> dict:
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)
    for route, latency_ms in pairs:
        if not isfinite(latency_ms) or latency_ms < 0:
            raise ValueError("latency_ms must be finite and non-negative")
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        p95[route] = ordered[ceil(0.95 * len(ordered)) - 1]

    slowest = max(p95, key=lambda route: p95[route]) if p95 else None
    return {"counts": counts, "p95": p95, "slowest": slowest}
