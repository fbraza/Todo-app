import click
from lib.actions import create_task, display_all_tasks, set_done, purge_done


@click.group()
def cli():
    pass


@cli.command()
@click.option("--title", required=True, help='Title of your task')
@click.option("--priority", default="Normal", help='Set the priority of your task, Normal by default')
def add(title, priority):
    """Create and add a task to your list"""
    create_task(title, priority)


@cli.command()
@click.option("--ordered", default='false', type=click.BOOL, help="if true show sorted list by priority, false by default")
@click.option("--all", default='true', type=click.BOOL, help='if true show all tasks else just the undone ones, false by default')
def display(ordered, all):
    """Output all registered tasks by default, see help for more details"""
    display_all_tasks(ordered, all)


@cli.command()
@click.option("--title", required=True, help='Title of your task')
def done(title):
    """Set a selected task as done"""
    set_done(title)


@cli.command()
def purge():
    """Suppress all done tasks"""
    purge_done()