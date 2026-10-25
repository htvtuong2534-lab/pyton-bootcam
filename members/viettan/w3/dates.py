import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a due date from ISO format or a simple relative expression."""
    value = text.strip().lower()

    if not value:
        raise ValueError("Due date cannot be empty")

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))

    weekdays = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6,
    }

    if value in weekdays:
        days_ahead = (weekdays[value] - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Invalid due date: {text!r}")
