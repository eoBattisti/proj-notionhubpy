from typing import Annotated, Optional
import typer
from rich.console import Console


from .table import TasksTable
from .entities import TaskItem, TaskToCreate
from cli.callbacks import get_api_obj_callback
from cli.settings import TASKS_DABASE_ID
from cli.utils import process_data


app = typer.Typer()


@app.command()
def list(
    ctx: typer.Context,
    daily: Annotated[bool, typer.Option(help="A flag to search/filter for today's tasks")] = False,
    weekly: Annotated[bool, typer.Option(help="A flag to search/filter for this week's tasks")] = False
):
    """List tasks from the Tasks Database""" 
    tasks = ctx.obj.query_tasks(daily=daily, weekly=weekly,)
    tasks = process_data(data=tasks, obj=TaskItem)
    table = TasksTable()
    table.fill_table(tasks)
    console = Console()
    console.print(table)


@app.command()
def create(
    title: Annotated[str, typer.Option(help="Title of the tasks to create")],
    notion: Optional[str] = typer.Option(None, callback=get_api_obj_callback, hidden=True), 
):
    """Creates a new task"""
    if notion:
        console = Console()
        task: TaskToCreate = TaskToCreate(database_id=TASKS_DABASE_ID, title=title)
        response = notion.create_tasks(task=task)
        if response.status_code == 200:
            console.print("Task created")
        else:
            console.print("Task not created")


if __name__ == "__main__":
    app()
