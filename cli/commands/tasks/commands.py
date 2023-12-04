from typing import Annotated
import typer
from rich.console import Console


from cli.base_table import BaseTable
from .entities import TaskToCreate
from cli.settings import TASKS_DABASE_ID, TASKS_FIELDS


app = typer.Typer()


@app.command()
def list(
    ctx: typer.Context,
    daily: Annotated[bool, typer.Option(help="A flag to search/filter for today's tasks")] = False,
    weekly: Annotated[bool, typer.Option(help="A flag to search/filter for this week's tasks")] = False
):
    """List tasks from the Tasks Database""" 
    tasks = ctx.obj.query_tasks(daily=daily, weekly=weekly,)
    table = BaseTable(fields=TASKS_FIELDS, data=tasks)
    table.fill_table()
    console = Console()
    console.print(table)


@app.command()
def create(
    ctx: typer.Context,
    title: Annotated[str, typer.Option(help="Title of the tasks to create")],
):
    """Creates a new task"""
    console = Console()
    task: TaskToCreate = TaskToCreate(database_id=TASKS_DABASE_ID, title=title)
    response = ctx.obj.create_tasks(task=task)
    if response.status_code == 200:
        console.print("Task created")
    else:
        console.print("Task not created")


if __name__ == "__main__":
    app()
