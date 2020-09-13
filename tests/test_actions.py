from ..lib.todo import Todo
import pytest
import pickle
import plyvel


@pytest.fixture(scope="module")
def db():
    plyvel.destroy_db("../taskdb")
    db = plyvel.DB("../taskdb", create_if_missing=True)
    tasks = (Todo("Buy bananas", "High"),
             Todo("Read new Batman comic", done=True),
             Todo("Schedule doctor appointment", "Low"))
    for task in tasks:
        db.put(bytes(task.description, encoding='utf-8'), pickle.dumps(task))
    yield db
    db.close()
    plyvel.destroy_db("../taskdb")


def test_store_tasks(db):
    list_keys = [key for key, _ in db.iterator()]
    assert len(list_keys) == 3


def test_display_all_task(db):
    for key, value in db.iterator():
        task = pickle.loads(db.get(key))
        marker = "\u2713" if task.done else " "
        assert task.__str__() == "[{}] : {} : {}".format(marker, task.description, task.priority)


def test_select_only_undone_task(db):
    selected_tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator() if not pickle.loads(db.get(key)).done]
    assert len(selected_tasks) == 2


def test_order_by_priority(db):
    tasks = sorted([pickle.loads(db.get(key)) for key, _ in db.iterator()])
    assert tasks[0] == Todo("Buy bananas", "High")
