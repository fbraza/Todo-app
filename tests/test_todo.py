from project.lib.todo import Todo
import pytest


task_1 = Todo("Do Shopping", "Low")
task_2 = Todo("Go Fishing", "Low")
DONE_MARKER, UNDONE_MARKER = "\u2713", " "
description, priority, done = task_1.description, task_1.priority, task_1.done


@pytest.mark.parametrize("input, expected", [(description, "Do Shopping"), (priority, "Low"), (done, False)])
def test_todo_attr(input, expected):
    assert input == expected


def test_set_done():
    task_2.set_done()
    assert task_2.done == True


def test_redefine_priority():
    task_2.redefine_priority("High")
    assert task_2.priority == "High"


def test_catching_test_redefine_priority_error():
    with pytest.raises(ValueError):
        task_2.redefine_priority("medium")


def test__str__():
    marker, desc, prio = DONE_MARKER, task_2.description, task_2.priority
    assert task_2.__str__() == f"[{marker}] : {desc} : {prio}"
