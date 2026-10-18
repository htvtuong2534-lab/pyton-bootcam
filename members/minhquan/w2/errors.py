import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Union

@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: str

def load_tasks(path: Union[str, Path]) -> list[Task]:
    """
    Reads a CSV file containing task entries and returns a list of Task objects.
    Raises ValueError with the line number if any row is invalid.
    """
    tasks = []
    
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        
        if header is None:
            raise ValueError("CSV file is empty")

        # Line 1 is the header, so data rows start at line 2
        for line_num, row in enumerate(reader, start=2):
            # Check row column count
            if len(row) != 4:
                raise ValueError(f"Line {line_num}: Expected 4 fields, got {len(row)}")

            title, importance_raw, effort_raw, deadline = [field.strip() for field in row]

            # Validate field types
            try:
                importance = int(importance_raw)
                effort_h = float(effort_raw)
            except ValueError as err:
                raise ValueError(f"Line {line_num}: Invalid numeric format - {err}") from err

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
    """
    Saves a list of Task objects into a JSON file at the specified path.
    """
    task_dicts = [
        asdict(task) if hasattr(task, "__dataclass_fields__") else task.__dict__
        for task in tasks
    ]
    
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(task_dicts, file, indent=4)