"""W1-5: group course codes by their timetable day."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Return sorted course lists for each day, preserving duplicate entries."""
    grouped: dict[str, list[str]] = {}
    for course, day in entries:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(courses) for day, courses in grouped.items()}
