import typer

from notion_api import NotionAPI
from settings import API_TOKEN, API_VERSION

from commands.birthdays.commands import app as birthday_app
from commands.tasks.commands import app as task_app


app = typer.Typer()
notion_api = NotionAPI(api_token=API_TOKEN,
                       notion_version=API_VERSION)

app.add_typer(typer_instance=birthday_app, name="birthday", help="List birthdays")
app.add_typer(typer_instance=task_app, name="tasks", help="List or create tasks")


if __name__ == "__main__":
    app()
