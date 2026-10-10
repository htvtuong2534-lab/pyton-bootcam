"""Additional checks for W1 cases not covered by the instructor's examples."""

import pytest

from members.phucloc.w1.grades import summary
from members.phucloc.w1.rules import can_register_thesis, missing
from members.phucloc.w1.text_tools import top_k, word_count
from members.phucloc.w1.timetable import by_day


def test_summary_rounds_an_odd_median_and_preserves_input():
    scores = [3.333, 1.111, 2.222]
    assert summary(scores) == {
        "min": 1.111,
        "max": 3.333,
        "mean": 2.22,
        "median": 2.22,
    }
    assert scores == [3.333, 1.111, 2.222]


def test_word_count_separates_all_required_punctuation():
    assert word_count("Git,is.fun!Git?is;fast:") == {
        "git": 2, "is": 2, "fun": 1, "fast": 1,
    }


def test_top_k_breaks_equal_counts_alphabetically():
    assert top_k("beta alpha beta alpha", 10) == [("alpha", 2), ("beta", 2)]


@pytest.mark.parametrize("k", [0, -1])
def test_top_k_non_positive_limit(k):
    assert top_k("hello hello", k) == []


@pytest.mark.parametrize("credits, gpa", [(119, 2.0), (120, 1.99)])
def test_thesis_requires_both_thresholds(credits, gpa):
    assert not can_register_thesis(credits, gpa)


def test_missing_explains_gpa_without_a_credit_reason():
    reasons = missing(120, 1.99)
    assert len(reasons) == 1
    assert "GPA" in reasons[0] and "2.0" in reasons[0]


def test_timetable_preserves_duplicates_and_input():
    entries = [("B", "Mon"), ("A", "Mon"), ("A", "Mon")]
    assert by_day(entries) == {"Mon": ["A", "A", "B"]}
    assert entries == [("B", "Mon"), ("A", "Mon"), ("A", "Mon")]
