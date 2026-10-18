import argparse
import sys
from pathlib import Path

from .io_untils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv_path", nargs="?", default=Path(__file__).with_name("tasks.csv")
    )
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.csv_path)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    for task in tasks:
        print(
            f"{task.title} | importance={task.importance} | "
            f"effort_h={task.effort_h:g} | deadline={task.deadline.isoformat()}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
