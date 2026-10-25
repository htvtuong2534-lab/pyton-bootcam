import argparse
import sys
from datetime import date
from pathlib import Path

from members.hienluong.w2.io_untils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a study plan from a CSV file."
    )

    parser.add_argument(
        "csv_file",
        type=Path,
        help="Path to the CSV file",
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study time in hours",
    )

    parser.add_argument(
        "--today",
        default=None,
        help="Reference date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    if args.hours <= 0:
        parser.error("--hours must be greater than 0")

    try:
        today = date.fromisoformat(args.today) if args.today else date.today()

        if not args.csv_file.is_file():
            raise FileNotFoundError(
                f"CSV file not found: {args.csv_file}"
            )

        tasks = load_tasks(args.csv_file)

        if not tasks:
            print("No tasks found.")
            return 0

        # Sort by deadline, importance, then effort.
        tasks.sort(
            key=lambda task: (
                task.deadline,
                -task.importance,
                task.effort_h,
            )
        )

        remaining_hours = args.hours
        selected_tasks = []

        for task in tasks:
            if task.effort_h <= remaining_hours:
                selected_tasks.append(task)
                remaining_hours -= task.effort_h

        print("=== Study Plan ===")
        print(f"Today: {today.isoformat()}")
        print(f"Available time: {args.hours:g} hours")

        for index, task in enumerate(selected_tasks, start=1):
            print(
                f"{index}. {task.title} | "
                f"Deadline: {task.deadline.isoformat()} | "
                f"Importance: {task.importance} | "
                f"Duration: {task.effort_h:g} hours"
            )

        planned_hours = args.hours - remaining_hours
        print(f"Total planned time: {planned_hours:g} hours")
        print(f"Unused time: {remaining_hours:g} hours")

    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())