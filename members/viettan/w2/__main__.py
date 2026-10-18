
from pathlib import Path

from members.viettan.w2.io_utils import load_tasks


def main():
    sample_csv = Path("sample_tasks.csv")

    if not sample_csv.exists():
        print(f"Sample CSV not found: {sample_csv}")
        return

    tasks = load_tasks(sample_csv)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
