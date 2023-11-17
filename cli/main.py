import typer

from cli.commands.birthdays.commands import app as birthday_app
from cli.commands.projects.commands import app as project_app
from cli.commands.tasks.commands import app as task_app


app = typer.Typer()

app.add_typer(typer_instance=birthday_app, name="birthday", help="List birthdays")
app.add_typer(typer_instance=task_app, name="tasks", help="List or create tasks")
app.add_typer(typer_instance=project_app, name="projects", help="List projects")
