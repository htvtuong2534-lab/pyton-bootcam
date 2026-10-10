# Phuc Loc - Week 1

Implemented from Section 18.5 of the CSC10014 Git & GitHub tutorial:

| Exercise | Module | Functions | Status |
| --- | --- | --- | --- |
| W1-1 | `grades.py` | `summary` | Implemented |
| W1-2 | `text_tools.py` | `word_count`, `top_k` | Implemented |
| W1-3 | `rules.py` | `can_register_thesis`, `missing` | Implemented |
| W1-4 | `translate.py` | `binary_search` (variant 1) | Implemented |
| W1-5 | `timetable.py` | `by_day` | Implemented |

The five empty `bai*.py` placeholders have been replaced by the module
names expected by the instructor's tests.

## Run the additional tests

From the repository root, with Python 3.10+ and pytest installed:

```sh
python -m pytest -q members/phucloc/w1/test_basics.py
```

These additional tests cover rounding, input preservation, punctuation,
alphabetical tie-breaking, non-positive limits, GPA/credit boundaries and
duplicate courses, binary-search boundaries and duplicate keys.

## Instructor tests

The repository's `tests/test_w1.py` is currently empty and
`tests/conftest.py` is missing. The team setup owner must copy both files
from `CSC10014-at-fit-hcmus/public_materials/python-bootcamp/tests/`.
After that, test all five completed exercises with:

```sh
python -m pytest -q tests/test_w1.py --member phucloc --variant 1
```

Loc confirmed W1-4 variant 1: translate the C++ binary-search function
without changing its behavior. Its docstring explains the required
difference between C++ and Python. Other code comments and docstrings
were removed at Loc's request.

Word counting treats the six specified punctuation marks as separators.
`top_k` returns no words for a non-positive limit. Grade rounding uses
Python's `round(value, 2)`, matching the instructor's example.

## AI use

Codex generated the implementation, additional tests and this explanation.
The assistance and verification are recorded in `docs/ai-use-log.md`.
Loc must read and understand the code before review, submission or defense;
the generated work is not represented as independently authored by Loc.
