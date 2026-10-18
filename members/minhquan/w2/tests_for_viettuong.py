import pytest
from members.viettuong.w1.grades import summary


def test_summary_normal():
    result = summary([8, 9, 10])
    assert result == {
        "min": 8,
        "max": 10,
        "mean": 9.0,
        "median": 9,
    }


def test_summary_even_number():
    result = summary([1, 2, 3, 4])
    assert result["median"] == 2.5


def test_summary_single_value():
    result = summary([7])
    assert result == {
        "min": 7,
        "max": 7,
        "mean": 7.0,
        "median": 7,
    }


def test_summary_unsorted_input():
    result = summary([10, 5, 8])
    assert result["min"] == 5
    assert result["max"] == 10
    assert result["median"] == 8


def test_summary_empty_list():
    with pytest.raises(ValueError):
        summary([])