import csv
import json
import os
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks: list[Task] = []

    with open(path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader, None)

        if header is None:
            return tasks

        expected_header = [column.strip().lower() for column in header]
        if expected_header != ["title", "importance", "effort_h", "deadline"]:
            raise ValueError("CSV header must be: title,importance,effort_h,deadline")

        for line_num, row in enumerate(reader, start=2):
            if len(row) != 4:
                raise ValueError(f"Invalid row at line {line_num}: expected 4 columns, got {len(row)}")

            title, importance_str, effort_str, deadline_str = (cell.strip() for cell in row)

            try:
                importance = int(importance_str)
                effort_h = float(effort_str)
                deadline = date.fromisoformat(deadline_str)
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid row at line {line_num}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    serialized = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(path, mode="w", encoding="utf-8") as json_file:
        json.dump(serialized, json_file, ensure_ascii=False, indent=4)
