def insertion_sort(a: list[int]) -> list[int]:
    """Sort a list in place and return it.

    Python modifies the original list directly, unlike a C++ function
    that returns a vector by value.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
