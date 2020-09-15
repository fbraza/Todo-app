from .todo import Todo
from os import system
import pickle
import plyvel


def create_task(title: str, priority: str, done: bool = False):
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


def display_all_tasks(ordered: bool, all: bool):
    """
    Function defined to display the tasks saved in the leveldb
    database.

    Parameters:
    -----------
    - ordered: bool, if True tasks will be orderer and display by priority
    - all: bool, if True all tasks including the one already done will be display

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


def select_task(title: str):
    """
    Function defined to select a task in order to modify its status

    Parameter:
    ----------
    title: str, title / description of the task

    Return:
    -------
    - Todo Object
    """
    db = plyvel.DB("./taskdb", create_if_missing=False)
    selected_task = [pickle.loads(db.get(key)) for key, _ in db.iterator() if key == bytes(title, encoding="utf-8")]
    try:
        if len(selected_task) == 0:
            raise ValueError("\nError:\nTask not found. Check if the task name is present or correctly spelt")
    except ValueError as message:
        print(message)
        return
    db.close()
    return selected_task[0]


def set_done(title: str):
    """
    Function defined to set a task done

    Parameter:
    ----------
    title: str, title / description of the task

    Return:
    -------
    - Todo Object
    """
    task = select_task(title)
    task.done = True
    db = plyvel.DB("./taskdb", create_if_missing=False)
    db.put(bytes(title, encoding="utf-8"), pickle.dumps(task))
    db.close()


def purge_done():
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
