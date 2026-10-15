
def day_by(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort course names."""
    days = {}

    for course, day in courses:
        if day not in days:
            days[day] = []
        days[day].append(course)

    return {
        day: sorted(course_list)
        for day, course_list in sorted(days.items())
    }