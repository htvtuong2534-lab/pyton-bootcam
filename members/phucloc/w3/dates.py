import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    value = text.strip().lower()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return date.fromisoformat(value)
        if value == "tomorrow":
            return today + timedelta(days=1)

        relative = re.fullmatch(r"in\s+(\d+)\s+days?", value)
        if relative:
            return today + timedelta(days=int(relative.group(1)))

        weekdays = (
            "monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday",
        )
        for index, name in enumerate(weekdays):
            if value in (name, name[:3]):
                offset = (index - today.weekday()) % 7 or 7
                return today + timedelta(days=offset)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"Invalid due date: {text!r}") from error

    raise ValueError(f"Unknown due date: {text!r}")
