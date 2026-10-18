from pathlib import Path

from .io_untils import load_tasks


def main():
    project_root = Path(__file__).resolve().parents[3]
    csv_file = project_root / "data" / "tasks.csv"

    if not csv_file.exists():
        print(f"CSV file not found: {csv_file}")
        return

    try:
        tasks = load_tasks(csv_file)
    except (ValueError, OSError) as error:
        print(f"Error loading tasks: {error}")
        return

    if not tasks:
        print("No tasks found.")
        return

    print("Study tasks:")
    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task.title} | "
            f"Importance: {task.importance} | "
            f"Effort: {task.effort_h} hours | "
            f"Deadline: {task.deadline.isoformat()}"
        )


if __name__ == "__main__":
    main()
