import argparse
import sys
from datetime import date
from pathlib import Path

try:
    from members.quocdat.w2.io_utils import load_tasks
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from members.quocdat.w2.io_utils import load_tasks


def pick_tasks(tasks, hours: float, today: date | None = None):
    if today is None:
        today = date.today()

    selected = []
    total = 0.0

    for task in sorted(tasks, key=lambda item: (item.deadline, -item.importance)):
        if total + task.effort_h <= hours:
            selected.append(task)
            total += task.effort_h

    return selected


def render_plan(tasks, hours: float) -> str:
    lines = [f"Tonight ({hours:.1f} h):"]

    if not tasks:
        lines.append("No tasks fit in the remaining time.")
        return "\n".join(lines)

    for index, task in enumerate(tasks, start=1):
        label = f"{index}. {task.title}"
        dots = "." * max(0, 28 - len(label))
        lines.append(f"{label}{dots} {task.effort_h:>4.1f} h")

    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Plan a study session for a day.")
    parser.add_argument("csv_path", help="Path to the tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Reference day in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args(argv)

    requested_today = args.today or date.today()

    csv_path = Path(args.csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    tasks = load_tasks(str(csv_path))
    tasks_for_tonight = pick_tasks(tasks, args.hours, requested_today)
    print(render_plan(tasks_for_tonight, args.hours))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FileNotFoundError as exc:
        raise SystemExit(f"Error: {exc}")
