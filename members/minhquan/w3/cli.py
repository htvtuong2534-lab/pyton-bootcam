import argparse
import csv
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Command-line tool for tasks.")

    parser.add_argument("filename", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Total available hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=date.today().isoformat(),
        help="Date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    file_path = Path(args.filename)
    if not file_path.is_file():
        print(f"Error: File '{args.filename}' not found.", file=sys.stderr)
        sys.exit(1)

    tasks = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    task_name = row[0].strip()
                    task_hours = float(row[1].strip())
                    tasks.append((task_name, task_hours))
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Tonight ({args.hours:.1f} h):")
    accumulated_hours = 0.0
    for idx, (name, task_h) in enumerate(tasks, 1):
        if accumulated_hours + task_h <= args.hours:
            print(f"  {idx}. {name:<12} ...... {task_h:.1f} h")
            accumulated_hours += task_h
        else:
            remaining = args.hours - accumulated_hours
            if remaining > 0:
                print(f"  {idx}. {name:<12} ...... {remaining:.1f} h")
            break


if __name__ == "__main__":
    main()