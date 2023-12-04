import typer
from rich.console import Console

from cli.base_table import BaseTable
from cli.settings import PROJECTS_FIELDS

app = typer.Typer()

@app.command()
def list(ctx: typer.Context):
    """List all projects"""
    projects = ctx.obj.query()
    table = BaseTable(fields=PROJECTS_FIELDS, data=projects)
    table.fill_table()
    console = Console()
    console.print(table)
