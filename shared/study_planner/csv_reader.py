
import csv
from datetime import date
from pathlib import Path

from shared.contract import StudyTask


def parse_csv(file_path):
    """Read tasks and preserve their importance values."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        if not file.read().strip():
                    raise ValueError("CSV contains no tasks")

        file.seek(0)
        reader = csv.DictReader(file)
        required = {"title", "importance", "effort_h", "deadline"}

        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain: title, importance, effort_h, deadline"
            )

        tasks = []

        for index, row in enumerate(reader, start=1):
            title = (row["title"] or "").strip()
            deadline = (row["deadline"] or "").strip()

            if not title:
                raise ValueError(f"Row {index}: title must not be empty")

            try:
                importance = int(row["importance"])
                effort_hours = float(row["effort_h"])
                date.fromisoformat(deadline)
            except (TypeError, ValueError) as error:
                raise ValueError(f"Invalid data on row {index}") from error

            if not 1 <= importance <= 5:
                raise ValueError(f"Row {index}: importance must be 1–5")
            if effort_hours <= 0:
                raise ValueError(f"Row {index}: effort_h must be positive")

            task = StudyTask(
                task_id=f"T{index:03}",
                title=title,
                subject="General",
                due_date=deadline,
                duration_minutes=round(effort_hours * 60),
            )

            tasks.append({
                "task": task,
                "importance": importance,
                "effort_hours": effort_hours,
            })

    if not tasks:
        raise ValueError("CSV contains no tasks")

    return tasks
