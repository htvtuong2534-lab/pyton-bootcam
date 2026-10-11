
def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether a student meets the thesis registration requirements."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return readable reasons when a student does not meet the requirements."""
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append("need GPA of at least 2.0")

    return reasons


if __name__ == "__main__":
    print(can_register_thesis(120, 2.5))
    print(can_register_thesis(118, 2.5))
    print(missing(118, 2.5))
    print(missing(118, 1.8))
    print(missing(120, 2.0))