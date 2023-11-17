from typing import Annotated
import typer
from rich.console import Console

from .api import TasksNotionAPI 
from .table import TasksTable
from .entities import TaskItem, TaskToCreate
from cli.utils import process_data


app = typer.Typer()
notion = TasksNotionAPI()

@app.command()
def list(daily: Annotated[bool, typer.Option(help="A flag to search/filter for today's tasks")] = False,
         weekly: Annotated[bool, typer.Option(help="A flag to search/filter for this week's tasks")] = False):
    """List tasks from the Tasks Database""" 
    tasks = notion.query_tasks(daily=daily, weekly=weekly,)
    tasks = process_data(data=tasks, obj=TaskItem)
    table = TasksTable()
    table.fill_table(tasks)
    console = Console()
    console.print(table)

@app.command()
def create(title: Annotated[str, typer.Option(help="Title of the tasks to create")]):
    """Creates a new task"""
    console = Console()
    task: TaskToCreate = TaskToCreate(database_id=TASKS_DABASE_ID, title=title)
    response = notion.create_tasks(task=task)
    if response.status_code == 200:
        console.print("Task created")
    else:
        console.print("Task not created")


if __name__ == "__main__":
    app()
