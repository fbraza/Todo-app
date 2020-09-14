import click
from lib.actions import create_task, display_all_tasks


@click.group()
def cli():
    pass


@cli.command()
@click.option("--title", required=True, help='Title of your task')
@click.option("--priority", default="Normal", help='Set the priority of your task')
def add(title, priority):
    create_task(title, priority)


@cli.command()
@click.option("--ordered", default='false', type=click.BOOL, help="if true show sorted list by priority, false by default")
@click.option("--all", default='false', type=click.BOOL, help='if true show all tasks else just the undone ones, false by default')
def display(ordered, all):
    display_all_tasks(ordered, all)
