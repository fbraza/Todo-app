from todo_app.lib.todo import Todo
import pytest
import pickle
import plyvel


@pytest.fixture(scope="module")
def db():
    db = plyvel.DB("../taskdb", create_if_missing=True)
    tasks = (Todo("Buy bananas", "High"),
             Todo("Read new Batman comic", done=True), 
             Todo("Schedule doctor appointment", "Low"))
    for task in tasks:
        db.put(bytes(task.description, encoding='utf-8'), pickle.dumps(task))
    yield db
    db.close()
    plyvel.destroy_db("../taskdb")


def test_storage(db):
    list_keys = []
    for key, _ in db.iterator():
        list_keys.append(key)
    assert len(list_keys) == 3


def test_display_all_task(db):
    for key, value in db.iterator():
        task = pickle.loads(db.get(key))
        marker = "\u2713" if task.done else " "
        assert task.__str__() == "[{}] : {} : {}".format(marker, task.description, task.priority)


def test_select_only_undone_task(db):
    selected_tasks = []
    for key, value in db.iterator():
        task = pickle.loads(db.get(key))
        if not task.done: 
            selected_tasks.append(task)
    assert len(selected_tasks) == 2


def test_order_by_priority(db):
    tasks = []
    for key, value in db.iterator():
        task = pickle.loads(db.get(key))
        tasks.append(task)
    tasks = sorted(tasks)
    assert tasks[0] == Todo("Buy bananas", "High")
