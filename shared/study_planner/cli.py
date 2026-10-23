
import argparse
import sys
from pathlib import Path

from .csv_reader import parse_csv
from .prioritise import prioritise
from .allocate import allocate, InfeasiblePlan
from .render import render


def main():
    parser = argparse.ArgumentParser(
        description="Generate a study plan from a CSV file."
    )
    parser.add_argument("csv_file", type=Path, help="Path to the CSV file")
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
        items = parse_csv(args.csv_file)

        from datetime import date

        today = (
            date.fromisoformat(args.today)
            if args.today
            else date.today()
        )

        ordered_items = prioritise(items, today)
        plan = allocate(ordered_items, args.hours)
        render(plan, args.hours)

    except (FileNotFoundError, ValueError, InfeasiblePlan) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
