import csv
import json
from datetime import date
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Bỏ qua dòng tiêu đề (header) đầu tiên
        header = next(reader, None)
        
        # Duyệt từng dòng, bắt đầu đếm số dòng từ 2 (sau header)
        for line_num, row in enumerate(reader, start=2):
            # Kiểm tra xem dòng có đủ 4 cột hay không
            if len(row) != 4:
                raise ValueError(f"Dòng lỗi ở hàng số {line_num}: Không đủ dữ liệu.")
            
            title_str, imp_str, effort_str, deadline_str = row
            
            try:
                importance_val = int(imp_str.strip())
                effort_val = float(effort_str.strip())
                deadline_val = date.fromisoformat(deadline_str.strip())
            except ValueError:
                # Nếu ép kiểu dữ liệu thất bại (ví dụ: chữ vào ô số, sai ngày tháng), raise ValueError kèm số dòng
                raise ValueError(f"Dòng lỗi ở hàng số {line_num}: Sai định dạng dữ liệu.")
            
            task = Task(
                title=title_str.strip(),
                importance=importance_val,
                effort_h=effort_val,
                deadline=deadline_val
            )
            tasks.append(task)
            
    return tasks

def save_json(tasks: list[Task], path: str):
    tasks_data = []
    for t in tasks:
        tasks_data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat() # Chuyển date thành chuỗi 'YYYY-MM-DD' để ghi ra JSON
        })
        
    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(tasks_data, file, ensure_ascii=False, indent=4)