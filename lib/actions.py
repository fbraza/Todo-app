from todo import Todo
from os import system
import pickle
import plyvel


def create_task(title, priority="Normal", done=False):
    """
    Function defined to leverage the Todo class constructor
    to instantiate a Todo object and save it in the leveldb
    database. The title is used as key and a serialized Todo
    object is stored as value.

    Parameters:
    -----------
    - title: str, describe the task
    - priority: str, priority of the task. Normal by defaut
    - done: bool, whether or not task is done. False by default

    Return:
    -------
    - None
    """
    db = plyvel.DB("../taskdb", create_if_missing=True)
    task = Todo(title, priority, done)
    db.put(bytes(task.description, encoding='utf-8'), pickle.dumps(task))
    db.close()


def display_all_tasks(ordered=False, all=False):
    """
    Function defined to display the tasks saved in the leveldb
    database.

    Parameters:
    -----------
    - ordered: str, if True tasks will be orderer and display by priority
    - all: str, if True all tasks including the one already done will be display

    Return:
    -------
    - None
    """
    db = plyvel.DB("../taskdb", create_if_missing=True)
    tasks = []
    # select tasks and close db
    if all:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator()]
    else:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator() if not pickle.loads(db.get(key)).done]
    db.close()
    # sort tasks if needed
    tasks = sorted(tasks) if ordered else tasks
    system("clear")
    print("------- Your taks -------\n")
    for task in tasks:
        print(task)