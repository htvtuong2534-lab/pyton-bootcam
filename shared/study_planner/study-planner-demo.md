# Team T-W3 Study Planner Demo

## Goal

Demonstrate how the team study planner converts a CSV task list into a study plan that fits the available time.

## Input

File: `members/viettan/w2/sample_tasks.csv`

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## Run

From the repository root:

```bash
python3 -m shared.study_planner members/viettan/w2/sample_tasks.csv --hours 2 --today 2026-10-26
```

## Expected Result

```text
=== Study Plan ===
Available time: 2 hours
1. Assignment | Subject: General | Duration: 90 minutes | Deadline: 2026-10-27 | Importance: 4
Total planned time: 90 minutes
Unused time: 30 minutes
```

## What This Demonstrates

1. `parse_csv` reads and validates the input tasks.
2. `prioritise` sorts tasks by deadline, importance, and effort.
3. `allocate` selects tasks that fit within two hours.
4. `render` displays the plan and remaining time.

## Error Handling Demo

A missing input file:

```bash
python3 -m shared.study_planner notfound.csv --hours 2
```

Expected message:

```text
Error: File not found: notfound.csv
```
