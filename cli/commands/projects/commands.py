import typer
from rich.console import Console

from cli.commands.projects.entities import ProjectsItem
from cli.commands.projects.table import ProjectsTable
from cli.utils import process_data

app = typer.Typer()

@app.command()
def list(ctx: typer.Context):
    """List all projects"""
    projects = ctx.obj.query()
    projects = process_data(data=projects, obj=ProjectsItem)
    table = ProjectsTable()
    table.fill_table(objects=projects)
    console = Console()
    console.print(table)
