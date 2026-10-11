# Python Bootcamp

A collaborative Python learning project for practicing programming fundamentals, Git, GitHub, and team development workflows.

## Project Overview

This repository contains weekly Python homework assignments and shared team code for a Study Planner application.

Team members complete individual exercises in their own folders, collaborate on shared modules, and track their progress through GitHub Issues, Pull Requests, and milestones.

## Repository Structure

```text
python-bootcamp/
├── README.md
├── PROGRESS.md
├── members/
│   ├── viettuong/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   ├── phucloc/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   ├── hienluong/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   ├── quocdat/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   ├── viettan/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   └── minhquan/
│       ├── w1/
│       ├── w2/
│       └── w3/
├── shared/
│   ├── contract.py
│   └── study_planner/
└── tests/
    ├── test_w1.py
    ├── test_w2.py
    └── test_w3.py
```

Each member folder contains individual weekly assignments. The `shared/` directory contains common code developed collaboratively by the team. The `tests/` directory is reserved for automated tests.

## Requirements

- Python 3.10 or later is recommended.
- Git
- GitHub account
- `pytest` for running automated tests

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd python-bootcamp
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the testing dependency:

```bash
python -m pip install pytest
```

## Running Tests

Run all tests:

```bash
python -m pytest -v
```

Run tests for a specific week:

```bash
python -m pytest tests/test_w1.py -v
python -m pytest tests/test_w2.py -v
python -m pytest tests/test_w3.py -v
```

Tests can only be collected and executed when the corresponding test files contain valid test functions. Empty test files do not verify the correctness of the assignments.

## Weekly Assignments

### Week 1 — Python Basics

Topics include:

- Variables and data types
- Conditional statements and loops
- Functions and default arguments
- Lists, tuples, dictionaries, and sets
- Strings, f-strings, and slicing
- List and dictionary comprehensions
- Input and output

Individual exercises:

| Exercise | File | Description |
|---|---|---|
| W1-1 | `grades.py` | Calculate grade summary statistics |
| W1-2 | `text_tools.py` | Count words and find the most frequent words |
| W1-3 | `rules.py` | Check thesis registration eligibility |
| W1-4 | `translate.py` | Translate an assigned C++ function into Python |
| W1-5 | `timetable.py` | Group courses by day and sort course codes |

Assignments are stored in each member's `members/<username>/w1/` directory.

### Week 2 — Shared Development

The team will extend the shared Study Planner code according to the Week 2 requirements.

### Week 3 — Extension and Integration

The team will extend, integrate, and test the shared project according to the Week 3 requirements.

## Team Workflow

1. Check the assigned homework and its GitHub Issue.
2. Work in the appropriate weekly assignment folder.
3. Use meaningful commit messages.
4. Push changes to your own branch when the team workflow requires branch-based development.
5. Open a Pull Request for review.
6. Address review feedback before merging.
7. Update `PROGRESS.md` with the actual issue, PR, reviewer, test results, and hours spent.

Follow the team's agreed branch protection and merge rules. Do not push directly to `main` if the team requires Pull Requests.

## Progress Tracking

The `PROGRESS.md` file records each member's weekly progress, including:

- GitHub Issue
- Pull Request
- Reviewer
- Test results
- Hours spent

GitHub milestones and labels are used to organize weekly homework and team tasks.

## Coding Guidelines

- Use descriptive function and variable names.
- Follow Python conventions, including PEP 8 where practical.
- Add docstrings to explain function purposes.
- Handle invalid inputs according to the assignment requirements.
- Keep individual homework separate from shared team code.
- Test changes before submitting a Pull Request.

## References

- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)
- [Git Documentation](https://git-scm.com/doc)

## License

This repository is intended for educational and collaborative learning purposes.