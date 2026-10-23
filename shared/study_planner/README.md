# Study Planner

A command-line study planner that reads tasks from a CSV file, prioritises them, allocates available study time, and displays the resulting plan.

## Features

- Parse study tasks from a CSV file.
- Prioritise tasks by deadline, importance, and effort.
- Allocate tasks within the available study time.
- Display the selected tasks and remaining time.
- Handle missing files, invalid input, and infeasible plans.

## Requirements

- Python 3.9 or later
- No third-party packages are required for the planner itself.

## CSV Format

The input CSV must contain these columns:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

- `title`: task name
- `importance`: importance level from 1 to 5
- `effort_h`: estimated effort in hours
- `deadline`: due date in `YYYY-MM-DD` format

## Usage

Run the command from the repository root:

```bash
python3 -m shared.study_planner members/viettan/w2/sample_tasks.csv --hours 2 --today 2026-10-26
```

Example output:

```text
=== Study Plan ===
Available time: 2 hours
1. Assignment | Subject: General | Duration: 90 minutes | Deadline: 2026-10-27 | Importance: 4
Total planned time: 90 minutes
Unused time: 30 minutes
```

The example uses a fixed reference date so the output is reproducible.

## Run Tests

From the repository root:

```bash
python3 -m pytest -q
```

## Pipeline

The planner follows this sequence:

`parse_csv → prioritise → allocate → render`
