import typer
from rich.console import Console
from cli.commands.projects.entities import ProjectsItem

from cli.commands.projects.table import ProjectsTable
from cli.commands.projects.api import ProjectsNotionAPI 
from cli.utils import process_data

app = typer.Typer()
notion_api = ProjectsNotionAPI()

@app.command()
def list():
    """List all projects"""
    projects = notion_api.query()
    projects = process_data(data=projects, obj=ProjectsItem)
    table = ProjectsTable()
    table.fill_table(objects=projects)
    console = Console()
    console.print(table)
