"""Shared data contract for the team's study planner."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class StudyTask:
    """Represent one task in a student's study plan.

    Args:
        task_id: Unique ID for this task.
        title: Short task description.
        subject: Course or subject name.
        due_date: Optional due date in ISO format (YYYY-MM-DD).
        duration_minutes: Estimated time needed, in minutes.
        completed: Whether the task has been completed.
    """

    task_id: str
    title: str
    subject: str
    due_date: Optional[str] = None
    duration_minutes: int = 30
    completed: bool = False

    def __post_init__(self) -> None:
        self.task_id = self.task_id.strip()
        self.title = self.title.strip()
        self.subject = self.subject.strip()

        if not self.task_id:
            raise ValueError("task_id must not be empty")
        if not self.title:
            raise ValueError("title must not be empty")
        if not self.subject:
            raise ValueError("subject must not be empty")
        if isinstance(self.duration_minutes, bool) or not isinstance(
            self.duration_minutes, int
        ):
            raise TypeError("duration_minutes must be an integer")
        if self.duration_minutes <= 0:
            raise ValueError("duration_minutes must be greater than zero")
        if not isinstance(self.completed, bool):
            raise TypeError("completed must be a bool")
        if self.due_date is not None:
            if not isinstance(self.due_date, str):
                raise TypeError("due_date must be a string or None")
            self.due_date = self.due_date.strip() or None


# Shared function contract implemented by shared.study_planner:
# add_task(tasks, task) -> StudyTask
# list_tasks(tasks, subject=None, completed=None) -> list[StudyTask]
# get_task(tasks, task_id) -> StudyTask | None
# mark_completed(tasks, task_id) -> bool
# remove_task(tasks, task_id) -> bool
# total_study_minutes(tasks, include_completed=True) -> int
