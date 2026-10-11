import pytest

from members.viettuong.w1.bai1 import summary
from members.viettuong.w1.bai2 import wordcount, topk
from members.viettuong.w1.bai3 import can_register_thesis, missing
from members.viettuong.w1.bai4 import transpose_matrix
from members.viettuong.w1.bai5 import by_day


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

def test_wordcount():
    assert wordcount("Git is fun. Git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_topk():
    assert topk("Git is fun. Git is fast!", 2) == [
        ("git", 2),
        ("is", 2),
    ]


def test_topk_empty_text():
    assert topk("", 3) == []


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


# W1-4: Matrix transpose

def test_transpose_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


def test_transpose_empty_matrix():
    assert transpose_matrix([]) == []
    assert transpose_matrix([[]]) == []


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
