from collections import Counter, defaultdict
import math


def analyse(pairs):
    counts = Counter()
    latencies = defaultdict(list)

    # Gom số request và độ trễ theo từng route
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {}

    for route, values in latencies.items():
        values.sort()

        # Nearest-rank percentile
        index = math.ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    # Route có p95 cao nhất
    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }


if __name__ == "__main__":
    data = [
        ("/students", 10),
        ("/students", 20),
        ("/students", 30),
        ("/students", 40),
        ("/fee", 100),
        ("/fee", 200),
        ("/fee", 300),
        ("/fee", 400),
    ]

    result = analyse(data)
    print(result)