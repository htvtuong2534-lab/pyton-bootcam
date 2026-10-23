
import pytest

from shared.contract import StudyTask
from shared.study_planner.planner import (
    add_task,
    list_tasks,
    get_task,
    mark_completed,
    remove_task,
    total_study_minutes,
)


def make_task(task_id, title="Study", subject="Math", minutes=60):
    return StudyTask(
        task_id=task_id,
        title=title,
        subject=subject,
        duration_minutes=minutes,
    )


def test_add_and_get_task():
    tasks = []
    task = make_task("T01")

    assert add_task(tasks, task) is task
    assert get_task(tasks, "T01") is task


def test_duplicate_task_id_is_rejected():
    tasks = [make_task("T01")]

    with pytest.raises(ValueError):
        add_task(tasks, make_task("T01", title="Another task"))


def test_list_tasks_filters_by_subject():
    tasks = [
        make_task("T01", subject="Math"),
        make_task("T02", subject="Physics"),
    ]

    assert [task.task_id for task in list_tasks(tasks, subject="Math")] == [
        "T01"
    ]


def test_mark_completed():
    tasks = [make_task("T01")]

    assert mark_completed(tasks, "T01") is True
    assert tasks[0].completed is True
    assert mark_completed(tasks, "missing") is False


def test_remove_task():
    tasks = [make_task("T01")]

    assert remove_task(tasks, "T01") is True
    assert tasks == []
    assert remove_task(tasks, "missing") is False


def test_total_study_minutes():
    first = make_task("T01", minutes=60)
    second = make_task("T02", minutes=90)
    second.completed = True
    tasks = [first, second]

    assert total_study_minutes(tasks) == 150
    assert total_study_minutes(tasks, include_completed=False) == 60
