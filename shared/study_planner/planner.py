
from shared.contract import StudyTask


def add_task(tasks, title, subject, duration):
    """Add a new study task."""
    task = StudyTask(title, subject, duration)
    tasks.append(task)


def list_tasks(tasks):
    """Return all study tasks."""
    return tasks


def complete_task(tasks, index):
    """Mark a task as completed using its index."""
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        return True

    return False
