import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text = text.strip()

    if not text:
        raise ValueError("Date cannot be empty")

    if text.lower() == "today":
        return today

    if text.lower() == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", text, re.IGNORECASE)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekdays = {
        "mon": 0,
        "monday": 0,
        "tue": 1,
        "tues": 1,
        "tuesday": 1,
        "wed": 2,
        "wednesday": 2,
        "thu": 3,
        "thur": 3,
        "thurs": 3,
        "thursday": 3,
        "fri": 4,
        "friday": 4,
        "sat": 5,
        "saturday": 5,
        "sun": 6,
        "sunday": 6,
    }

    weekday_text = text.lower()
    if weekday_text in weekdays:
        target = weekdays[weekday_text]
        days_ahead = (target - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(text)
    except ValueError as error:
        raise ValueError(
            f"Invalid date: {text!r}. Use YYYY-MM-DD, "
            "'tomorrow', 'in 3 days', or a weekday such as 'Fri'."
        ) from error