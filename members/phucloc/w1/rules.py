"""W1-3: check the stated credit and GPA requirements for a thesis."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """A student is eligible with at least 120 credits and a GPA of 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List unmet requirements, with credits before GPA."""
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need GPA of at least 2.0 (current: {gpa:g})")
    return reasons
