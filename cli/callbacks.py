import typer

from .notion_api import NotionBaseAPI
from cli.commands.tasks.api import TasksNotionAPI  # noqa: F401
from cli.commands.projects.api import ProjectsNotionAPI  # noqa: F401 
from cli.commands.birthday.api import BirthdayNotionAPI  # noqa: F401


def get_api_obj_callback(ctx: typer.Context) -> NotionBaseAPI:
    for cls in NotionBaseAPI.__subclasses__():
        if ctx.parent.invoked_subcommand in cls.__name__.lower():
            ctx.obj = cls()
