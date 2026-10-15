import pytest

from members.quocdat.w1.grades import summary
from members.quocdat.w1.text_tools import word_count, top_k
from members.quocdat.w1.rules import can_register_thesis, missing
from members.quocdat.w1.translate import insertion_sort
from members.quocdat.w1.timetable import by_day


# W1-1: Score summary

def test_summary():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_odd_length():
    result = summary([5, 7, 9])
    assert result["median"] == 7


def test_summary_empty():
    with pytest.raises(ValueError):
        summary([])


# W1-2: Word count and top-k

def test_word_count():
    assert word_count("Git is fun. Git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_top_k():
    assert top_k("Git is fun. Git is fast!", 2) == [
        ("git", 2),
        ("is", 2),
    ]


def test_top_k_empty_text():
    assert top_k("", 3) == []


# W1-3: Thesis registration rules

def test_can_register_thesis():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 3.0) is False
    assert can_register_thesis(120, 1.9) is False


def test_missing():
    assert missing(118, 2.5) == ["need 2 more credits"]
    assert missing(120, 1.5) == [
        "need GPA of at least 2.0 (current: 1.5)"
    ]
    assert missing(120, 2.0) == []


# W1-4: Insertion sort

def test_insertion_sort():
    assert insertion_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_insertion_sort_empty():
    assert insertion_sort([]) == []


# W1-5: Group courses by day

def test_by_day():
    entries = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]

    assert by_day(entries) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }


def test_by_day_empty():
    assert by_day([]) == {}
