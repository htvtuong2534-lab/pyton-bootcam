from members.hienluong.w1.translate import fibonacci


def test_fibonacci_zero_terms():
    assert fibonacci(0) == []


def test_fibonacci_one_term():
    assert fibonacci(1) == [0]


def test_fibonacci_two_terms():
    assert fibonacci(2) == [0, 1]


def test_fibonacci_ten_terms():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_negative_count():
    assert fibonacci(-3) == []


def test_fibonacci_large_integers():
    numbers = fibonacci(100)
    assert len(numbers) == 100
    assert numbers[-1] == 218922995834555169026


def test_fibonacci_calls_return_independent_lists():
    first = fibonacci(5)
    first[0] = 999
    first.append(999)
    assert fibonacci(5) == [0, 1, 1, 2, 3]
