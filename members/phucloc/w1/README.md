# Phuc Loc - Week 1

Implemented from Section 18.5 of the CSC10014 Git & GitHub tutorial:

| Exercise | Module | Functions | Status |
| --- | --- | --- | --- |
| W1-1 | `grades.py` | `summary` | Implemented |
| W1-2 | `text_tools.py` | `word_count`, `top_k` | Implemented |
| W1-3 | `rules.py` | `can_register_thesis`, `missing` | Implemented |
| W1-4 | `translate.py` | Depends on the assigned algorithm | Awaiting team-leader assignment |
| W1-5 | `timetable.py` | `by_day` | Implemented |

The four corresponding empty `bai*.py` placeholders have been replaced by
the module names expected by the instructor's tests. `bai4.py` remains
unchanged until the W1-4 assignment is known.

## Run the additional tests

From the repository root, with Python 3.10+ and pytest installed:

```sh
python -m pytest -q members/phucloc/w1/test_basics.py
```

These additional tests cover rounding, input preservation, punctuation,
alphabetical tie-breaking, non-positive limits, GPA/credit boundaries and
duplicate courses.

## Instructor tests

The repository's `tests/test_w1.py` is currently empty and
`tests/conftest.py` is missing. The team setup owner must copy both files
from `CSC10014-at-fit-hcmus/public_materials/python-bootcamp/tests/`.
After that, test the four completed exercises with:

```sh
python -m pytest -q tests/test_w1.py --member phucloc -k "not w1_4"
```

W1-4 is deliberately excluded because its algorithm has not been assigned.
Once it is implemented, remove `-k "not w1_4"` and pass the assigned
`--variant` value. An extra algorithm for a six-member team may require
an additional test agreed with the team leader.

Word counting treats the six specified punctuation marks as separators.
`top_k` returns no words for a non-positive limit. Grade rounding uses
Python's `round(value, 2)`, matching the instructor's example.

## AI use

Codex generated the implementation, additional tests and this explanation.
The assistance and verification are recorded in `docs/ai-use-log.md`.
Loc must read and understand the code before review, submission or defense;
the generated work is not represented as independently authored by Loc.
