import typer
from rich.console import Console

from notion_api import NotionAPI
from settings import API_TOKEN, API_VERSION, BIRTHDAY_DATABASE_ID
from commands.birthdays.table import BirthdayTable


app = typer.Typer()
notion = NotionAPI(api_token=API_TOKEN, notion_version=API_VERSION)

@app.command()
def list():
    """List all birthdays"""
    birthdays = notion.query_bithdays(database_id=BIRTHDAY_DATABASE_ID) 
    table = BirthdayTable()
    table.fill_table(birthdays)
    console = Console()
    console.print(table)
