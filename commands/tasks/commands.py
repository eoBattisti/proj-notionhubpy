from typing import Annotated
import typer
from rich.console import Console

from notion_api import NotionAPI
from settings import API_VERSION, API_TOKEN, TASKS_DABASE_ID

from .table import TasksTable
from .entities import TaskToCreate


app = typer.Typer()
notion = NotionAPI(api_token=API_TOKEN, notion_version=API_VERSION)

@app.command()
def list(daily: Annotated[bool, typer.Option(help="A flag to search/filter for today's tasks")] = False,
         weekly: Annotated[bool, typer.Option(help="A flag to search/filter for this week's tasks")] = False):
    """List tasks from the Tasks Database""" 
    tasks = notion.query_tasks(database_id=TASKS_DABASE_ID,
                               daily=daily,
                               weekly=weekly,)
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
