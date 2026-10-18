import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks: list[Task] = []
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        try:
            fields = reader.fieldnames
            expected = {"title", "importance", "effort_h", "deadline"}
            if fields is None or len(fields) != 4 or set(fields) != expected:
                raise ValueError(
                    "line 1: expected title,importance,effort_h,deadline header"
                )

            for row in reader:
                try:
                    if None in row or any(value is None for value in row.values()):
                        raise ValueError("missing or extra CSV fields")
                    task = Task(
                        title=row["title"].strip(),
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"].strip()),
                    )
                except (TypeError, ValueError) as error:
                    raise ValueError(f"line {reader.line_num}: {error}") from error
                tasks.append(task)
        except csv.Error as error:
            raise ValueError(
                f"line {max(reader.line_num, 1)}: invalid CSV: {error}"
            ) from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    records = [
        {**asdict(task), "deadline": task.deadline.isoformat()} for task in tasks
    ]
    Path(path).write_text(
        json.dumps(records, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
