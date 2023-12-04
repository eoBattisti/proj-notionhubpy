import typer
from rich.console import Console

from cli.base_table import BaseTable
from cli.settings import BIRTHDAY_FIELDS


app = typer.Typer()

@app.command()
def list(ctx: typer.Context):
    """List all birthdays"""
    birthdays = ctx.obj.query()
    print(BIRTHDAY_FIELDS)
    table = BaseTable(fields=BIRTHDAY_FIELDS, data=birthdays)
    table.fill_table()
    console = Console()
    console.print(table)

