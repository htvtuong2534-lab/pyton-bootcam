def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether a student meets thesis registration requirements."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons why requirements are not met."""
    reasons = []
    if credits < 120:
        remaining = 120 - credits
        reasons.append(f"need {remaining} more credit{'s' if remaining != 1 else ''}")
    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")
    return reasons
