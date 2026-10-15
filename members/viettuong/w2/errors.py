from typing import List
from .models import Task  # Import Task từ models.py cùng thư mục

class InfeasiblePlan(Exception):
    """Ngoại lệ tùy chỉnh khi kế hoạch công việc không khả thi (thiếu thời gian)."""
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        # Thông báo lỗi chi tiết khi exception được in ra
        super().__init__(
            f"Kế hoạch không khả thi! Cần tới {needed_h} giờ nhưng chỉ có {available_h} giờ."
        )

def check_feasible(tasks: List[Task], available_h: float):
    """Kiểm tra xem tổng số giờ làm task có vượt quá số giờ cho phép không."""
    # Tính tổng effort_h của tất cả các task trong danh sách
    total_needed = sum(task.effort_h for task in tasks)
    
    # Nếu vượt quá giờ có sẵn, ném ra ngoại lệ InfeasiblePlan
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)