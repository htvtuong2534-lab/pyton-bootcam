
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def day_left(self, today: date) -> int:
        delta = (self.deadline - today).days
        return max(0, delta)
