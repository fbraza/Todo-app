from todo import Todo
from os import system
import pickle
import plyvel


def create_task(title, priority="Normal", done=False):
    db = plyvel.DB("../taskdb", create_if_missing=True)
    task = Todo(title, priority, done)
    db.put(bytes(task.description, encoding='utf-8'), pickle.dumps(task))
    db.close()


def display_all_tasks(ordered=False, all=False):
    db = plyvel.DB("../taskdb", create_if_missing=True)
    tasks = []
    # select tasks
    if all:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator()]
    else:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator() if not pickle.loads(db.get(key)).done]
    db.close()
    # sort them
    tasks = sorted(tasks) if ordered else tasks
    system("clear")
    print("------- Your taks -------\n")
    for task in tasks:
        print(task)


create_task("Buy Banana", "High")
create_task("Bake banana cake")

display_all_tasks()