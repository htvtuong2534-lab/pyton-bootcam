import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text_clean = text.strip()

    try:
        return date.fromisoformat(text_clean)
    except ValueError:
        pass

    if text_clean.lower() == "tomorrow":
        return today + timedelta(days=1)

    match = re.match(r"^in\s+(\d+)\s+days?$", text_clean, re.IGNORECASE)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    weekdays_lower = [day.lower() for day in weekdays]

    if text_clean.lower() in weekdays_lower:
        target_weekday = weekdays_lower.index(text_clean.lower())
        current_weekday = today.weekday()

        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")