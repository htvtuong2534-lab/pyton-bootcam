from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def days_left(self, today: date) -> int:
        days = (self.deadline - today).days
        return max(days, 0)