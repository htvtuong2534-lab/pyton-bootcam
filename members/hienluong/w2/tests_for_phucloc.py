import pytest

from members.phucloc.w1.grades import summary
from members.phucloc.w1.rules import can_register_thesis, missing
from members.phucloc.w1.text_tools import word_count, top_k
from members.phucloc.w1.timetable import by_day
from members.phucloc.w1.translate import binary_search


def test_summary_normal_scores():
    result = summary([7.5, 9, 6, 8])
    assert result == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_empty_scores():
    with pytest.raises(ValueError, match="scores must not be empty"):
        summary([])


def test_can_register_thesis_at_minimum_requirements():
    assert can_register_thesis(120, 2.0) is True


def test_missing_both_requirements():
    assert missing(100, 1.5) == [
        "need 20 more credits",
        "need GPA of at least 2.0 (current: 1.5)",
    ]


def test_word_count_ignores_case_and_punctuation():
    assert word_count("Hello, hello! WORLD.") == {
        "hello": 2,
        "world": 1,
    }


def test_top_k_zero_returns_empty_list():
    # Edge case: k = 0
    assert top_k("apple apple banana", 0) == []


def test_by_day_sorts_courses():
    assert by_day([
        ("Math", "Monday"),
        ("English", "Monday"),
        ("Physics", "Tuesday"),
    ]) == {
        "Monday": ["English", "Math"],
        "Tuesday": ["Physics"],
    }


def test_binary_search_empty_list():
    assert binary_search([], 10) == -1
