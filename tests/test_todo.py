# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

# imports
from lib.todo import Todo
import pytest

DONE_MARKER, UNDONE_MARKER = "\u2713", " "
task_1 = Todo("Do Shopping")
task_2 = Todo("Go Fishing", "Low")
description_1, priority_1, done_1 = task_1.description, task_1.priority, task_1.done


@pytest.mark.parametrize("input, expected", [(description_1, "Do Shopping"), (priority_1, "Normal"), (done_1, False)])
def test_task_1_attr(input, expected):
    assert input == expected


def test_constructor_error():
    with pytest.raises(ValueError):
        Todo("Do the test", priority="Medium")


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
    assert task_2.__str__() == "[{}] : {} : {}".format(marker, desc, prio)

