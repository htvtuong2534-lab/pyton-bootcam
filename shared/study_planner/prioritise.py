
from datetime import date


def prioritise(items, today=None):
    """Sort tasks by urgency, importance, then shorter effort."""
    if today is None:
        today = date.today()

    def sort_key(item):
        task = item["task"]
        deadline = date.fromisoformat(task.due_date)
        days_left = (deadline - today).days

        return (
            days_left,
            -item["importance"],
            item["effort_hours"],
        )

    return sorted(items, key=sort_key)
