from members.viettan.w1.grades import summary
from members.viettan.w1.rules import can_register_thesis, missing
from members.viettan.w1.text_tools import top_k, word_count
from members.viettan.w1.timetable import by_day
from members.viettan.w1.translate import fibonacci


def test_summary_rounds_mean_and_median_for_unsorted_scores():
    assert summary([4.444, 1.111, 2.222]) == {
        "min": 1.111,
        "max": 4.444,
        "mean": 2.59,
        "median": 2.22,
    }


def test_word_count_is_case_insensitive_and_ignores_punctuation():
    assert word_count("Python, PYTHON! tests?") == {
        "python": 2,
        "tests": 1,
    }


def test_top_k_breaks_frequency_ties_alphabetically():
    assert top_k("pear plum apple", 2) == [("apple", 1), ("pear", 1)]


def test_thesis_registration_reports_both_missing_requirements():
    assert can_register_thesis(120, 2.0) is True
    assert missing(118, 1.5) == [
        "need 2 more credits",
        "need GPA of at least 2.0",
    ]


def test_fibonacci_returns_empty_for_negative_count():
    assert fibonacci(-1) == []


def test_by_day_sorts_each_day_without_merging_different_days():
    assert by_day(
        [
            ("ZOO20000", "Mon"),
            ("CSC10001", "Mon"),
            ("ZOO20000", "Tue"),
        ]
    ) == {
        "Mon": ["CSC10001", "ZOO20000"],
        "Tue": ["ZOO20000"],
    }
