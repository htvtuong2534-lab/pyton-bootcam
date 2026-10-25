import argparse
import sys
from datetime import date
from math import isfinite

from ..w2.io_untils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat)
    args = parser.parse_args()

    if not isfinite(args.hours) or args.hours < 0:
        parser.error("hours must be a finite non-negative number")
    today = args.today if args.today is not None else date.today()

    try:
        tasks = load_tasks(args.csv_path)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    ordered = sorted(
        tasks,
        key=lambda task: (
            -task.importance / max(task.days_left(today), 1),
            task.deadline,
            task.title,
        ),
    )
    remaining = args.hours
    print(f"Tonight ({args.hours:.1f} h):")
    count = 0
    for task in ordered:
        if remaining <= 0:
            break
        hours = min(task.effort_h, remaining)
        if hours <= 0:
            continue
        count += 1
        print(f"  {count}. {task.title} ...... {hours:g} h")
        remaining = max(0.0, remaining - hours)

    if count == 0:
        print("  No study time allocated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
