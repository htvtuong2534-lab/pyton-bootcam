
class InfeasiblePlan(Exception):
    """Raised when no task can fit into the available study time."""


def allocate(items, hours):
    """Select tasks that fit within the available study hours."""
    if hours <= 0:
        raise ValueError("hours must be greater than 0")

    available_minutes = int(hours * 60)
    selected = []
    used_minutes = 0

    for item in items:
        duration = item["task"].duration_minutes

        if used_minutes + duration <= available_minutes:
            selected.append(item)
            used_minutes += duration

    if not selected:
        raise InfeasiblePlan(
            "No task fits within the available study time"
        )

    return selected
