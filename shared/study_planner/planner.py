
from shared.contract import StudyTask


def add_task(tasks, task):
    """Add a StudyTask to the list."""
    if not isinstance(task, StudyTask):
        raise TypeError("task must be a StudyTask")

    if any(item.task_id == task.task_id for item in tasks):
        raise ValueError(f"Task ID already exists: {task.task_id}")

    tasks.append(task)
    return task


def list_tasks(tasks, subject=None, completed=None):
    """Return tasks filtered by subject and completion status."""
    result = tasks

    if subject is not None:
        result = [
            task for task in result
            if task.subject.lower() == subject.lower()
        ]

    if completed is not None:
        result = [
            task for task in result
            if task.completed == completed
        ]

    return result


def get_task(tasks, task_id):
    """Find a task by ID; return None if it does not exist."""
    for task in tasks:
        if task.task_id == task_id:
            return task

    return None


def mark_completed(tasks, task_id):
    """Mark a task as completed."""
    task = get_task(tasks, task_id)

    if task is None:
        return False

    task.completed = True
    return True


def remove_task(tasks, task_id):
    """Remove a task by ID."""
    task = get_task(tasks, task_id)

    if task is None:
        return False

    tasks.remove(task)
    return True


def total_study_minutes(tasks, include_completed=True):
    """Calculate total study time in minutes."""
    return sum(
        task.duration_minutes
        for task in tasks
        if include_completed or not task.completed
    )
