import typer
from rich.console import Console

from cli.commands.birthday.entities import BirthdayItem
from cli.commands.birthday.table import BirthdayTable
from cli.utils import process_data


app = typer.Typer()

@app.command()
def list(ctx: typer.Context):
    """List all birthdays"""
    birthdays = ctx.obj.query()
    birthdays = process_data(data=birthdays, obj=BirthdayItem)
    table = BirthdayTable()
    table.fill_table(birthdays)
    console = Console()
    console.print(table)

