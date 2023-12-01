import typer

from cli.commands.birthday.commands import app as birthday_app
from cli.commands.projects.commands import app as project_app
from cli.commands.tasks.commands import app as task_app
from .callbacks import get_api_obj_callback

app = typer.Typer()


app.add_typer(typer_instance=birthday_app, name="birthday", help="List birthdays", callback=get_api_obj_callback)
app.add_typer(typer_instance=task_app, name="tasks", help="List or create tasks", callback=get_api_obj_callback)
app.add_typer(typer_instance=project_app, name="projects", help="List projects", callback=get_api_obj_callback)
