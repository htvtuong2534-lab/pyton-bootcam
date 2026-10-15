
def can_register(credits: int, gpa: float) -> bool:
    """Check whether a student can register for the thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return reasons why the student cannot register."""
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons