
def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers.
    
    Python returns a list, while C++ typically uses a vector.
    """
    if n <= 0:
        return []

    numbers = []
    a, b = 0, 1

    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b

    return numbers