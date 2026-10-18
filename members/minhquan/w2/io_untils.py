import csv
import json
from datetime import date
from pathlib import Path
from typing import Union

from models import Task


def load_tasks(path: Union[str, Path]) -> list[Task]:
    tasks = []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)

        if header is None:
            raise ValueError("Dòng 1: File CSV rỗng")

        for line_num, row in enumerate(reader, start=2):
            if len(row) != 4:
                raise ValueError(
                    f"Dòng {line_num}: Yêu cầu 4 cột dữ liệu, nhưng tìm thấy {len(row)} cột"
                )

            title, importance_raw, effort_raw, deadline_raw = [
                field.strip() for field in row
            ]

            try:
                importance = int(importance_raw)
                effort_h = float(effort_raw)
                deadline = date.fromisoformat(deadline_raw)
            except ValueError as err:
                raise ValueError(
                    f"Dòng {line_num}: Định dạng dữ liệu không hợp lệ - {err}"
                ) from err

            tasks.append(
                Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            )

    return tasks


def save_json(tasks: list[Task], path: Union[str, Path]) -> None:
    task_dicts = []
    for task in tasks:
        task_dicts.append(
            {
                "title": task.title,
                "importance": task.importance,
                "effort_h": task.effort_h,
                "deadline": (
                    task.deadline.isoformat()
                    if isinstance(task.deadline, date)
                    else str(task.deadline)
                ),
            }
        )

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(task_dicts, file, indent=4, ensure_ascii=False)