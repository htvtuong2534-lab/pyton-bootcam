
import pytest

from members.quocdat.w1.grades import summary
from members.quocdat.w1.text_tools import word_count, top_k
from members.quocdat.w1.rules import can_register_thesis, missing
from members.quocdat.w1.translate import insertion_sort
from members.quocdat.w1.timetable import by_day


def test_summary_single_score():
    result = summary([8])
    assert result["min"] == 8
    assert result["max"] == 8
    assert result["mean"] == 8
    assert result["median"] == 8


def test_word_count_case_insensitive():
    assert word_count("Git git GIT") == {"git": 3}


def test_top_k_zero():
    assert top_k("apple banana apple", 0) == []


def test_can_register_thesis_boundary():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 2.0) is False


def test_insertion_sort_duplicates():
    assert insertion_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_by_day_empty():
    assert by_day([]) == {}
