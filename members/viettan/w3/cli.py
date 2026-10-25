import argparse
import sys
from datetime import date
from pathlib import Path

from members.viettan.w2.io_utils import load_tasks, save_json
from members.viettan.w3.dates import parse_due


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument(
        "-o", "--output",
        default="tasks.json",
        help="Path to output JSON file (default: tasks.json)",
    )
    parser.add_argument(
        "--today",
        help="Override today's date (YYYY-MM-DD)",
    )
    args = parser.parse_args(argv)

    try:
        today = (
            parse_due(args.today, date.today())
            if args.today
            else date.today()
        )
        input_path = Path(args.input)
        if not input_path.is_file():
            print(f"Error: input file not found: {input_path}", file=sys.stderr)
            return 1

        tasks = load_tasks(input_path)
        save_json(tasks, args.output)
        print(f"Loaded {len(tasks)} tasks; saved to {args.output}")
        return 0

    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
