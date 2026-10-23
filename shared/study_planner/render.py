
def render(plan, hours):
    """Display the selected study plan."""
    print("=== Study Plan ===")
    print(f"Available time: {hours:g} hours")

    total_minutes = 0

    for index, item in enumerate(plan, start=1):
        task = item["task"]
        duration = task.duration_minutes
        total_minutes += duration

        print(
            f"{index}. {task.title} "
            f"| Subject: {task.subject} "
            f"| Duration: {duration} minutes "
            f"| Deadline: {task.due_date} "
            f"| Importance: {item['importance']}"
        )

    print(f"Total planned time: {total_minutes} minutes")
    print(f"Unused time: {hours * 60 - total_minutes:g} minutes")
