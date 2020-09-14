from .todo import Todo
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
    db = plyvel.DB("./taskdb", create_if_missing=True)
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
    db = plyvel.DB("./taskdb", create_if_missing=True)
    tasks = []
    # select tasks
    if all:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator()]
    else:
        tasks = [pickle.loads(db.get(key)) for key, _ in db.iterator() if not pickle.loads(db.get(key)).done]
    # close the database
    db.close()
    # sort tasks if needed
    tasks = sorted(tasks) if ordered else tasks
    if not tasks:
        print("You have no task registered. Add one. See --help")
    else:
        print("------- Your taks -------\n")
        for task in tasks:
            print(task)


def redifine_priority(task_title, new_priority):
    """
    Function defined to fetch data from, modify it and put it back to the database.

    Parameters:
    -----------
    - task_title: str, description of the task, used as key in the database
    - new_priority: str, new value for the priority attribute of our Todo object
    Return:
    -------
    - None
    """
    db = plyvel.DB("./taskdb", create_if_missing=False)
    task_to_modify = db.get(bytes(task_title, encoding="utf-8"))
    if task_to_modify is None:
        db.close()
        raise ValueError("Unexisting or mispelled task. To see all your task do...")
    else:
        task_to_modify = pickle.loads(task_to_modify)
        task_to_modify.priority = new_priority
        db.put(bytes(task_title, encoding="utf-8"), pickle.dumps(task_to_modify))
        db.close()


def purge_databe():
    """
    Function defined to delete all done tasks.

    Return:
    -------
    - None
    """
    db = plyvel.DB("./taskdb", create_if_missing=False)
    tasks_to_delete = [key for key, _ in db.iterator() if pickle.loads(db.get(key)).done]
    for key in tasks_to_delete:
        db.delete(key)
    db.close()