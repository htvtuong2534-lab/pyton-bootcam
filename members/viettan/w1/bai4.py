
def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers.
    
    Unlike a typical fixed-size C++ array, a Python list can grow dynamically.
    """
    if n <= 0:
        return []

    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[:n]


if __name__ == "__main__":
    print(fibonacci(7))
    print(fibonacci(1))
    print(fibonacci(0))