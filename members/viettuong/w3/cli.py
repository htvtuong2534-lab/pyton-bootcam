
import argparse
import sys
from datetime import date
from pathlib import Path

from members.viettuong.w2.io_untils import load_tasks


def main():
    parser = argparse.ArgumentParser(
        description="Load study tasks from a CSV file."
    )

    parser.add_argument(
        "csv_file",
        type=Path,
        help="Path to the tasks CSV file",
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )

    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Reference date (default: today)",
    )

    args = parser.parse_args()

    if args.hours <= 0:
        parser.error("--hours must be greater than 0")

    if not args.csv_file.is_file():
        print(
            f"Error: file not found: {args.csv_file}",
            file=sys.stderr,
        )
        return 1

    try:
        tasks = load_tasks(str(args.csv_file))
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Loaded {len(tasks)} tasks")

    for task in tasks:
        print(
            f"- {task.title} | "
            f"Importance: {task.importance} | "
            f"Effort: {task.effort_h} hours | "
            f"Days left: {task.day_left(args.today)}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
