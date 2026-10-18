from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    sample_csv = Path(__file__).with_name("tasks.csv")
    tasks = load_tasks(str(sample_csv))
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
