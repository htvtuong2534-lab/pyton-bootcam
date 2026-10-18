
import csv
import json
from datetime import date

from members.viettan.w2.models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"title", "importance", "effort_h", "deadline"}

        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise ValueError("Invalid CSV header at line 1")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                if not task.title or task.importance < 0 or task.effort_h < 0:
                    raise ValueError("Invalid task values")
                tasks.append(task)
            except (ValueError, TypeError, KeyError, AttributeError) as exc:
                raise ValueError(
                    f"Invalid row at line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks, path) -> None:
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
