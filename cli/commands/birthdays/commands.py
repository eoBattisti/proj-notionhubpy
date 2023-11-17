import typer
from rich.console import Console
from cli.commands.birthdays.entities import BirthdayItem

from cli.commands.birthdays.table import BirthdayTable
from cli.commands.birthdays.api import BirthdayNotionAPI
from cli.utils import process_data


app = typer.Typer()
notion = BirthdayNotionAPI()

@app.command()
def list():
    """List all birthdays"""
    birthdays = notion.query()
    birthdays = process_data(data=birthdays, obj=BirthdayItem)
    table = BirthdayTable()
    table.fill_table(birthdays)
    console = Console()
    console.print(table)
