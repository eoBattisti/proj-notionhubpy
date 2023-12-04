import typer
from typer.testing import CliRunner

from .utils import generate_tasks
from cli.commands.tasks.commands import app
from cli.commands.tasks.entities import TaskToCreate


class FakeTaskAPI:

    def query_tasks(self, daily: bool, weekly: bool):
        data = generate_tasks()
        return data

    def create_tasks(self, task: TaskToCreate):
        pass


def get_fake_api_obj_callback(ctx: typer.Context):
    ctx.obj = FakeTaskAPI()


def test_tasks_list_with_no_opts(cli_runner: CliRunner):
    app.callback()(get_fake_api_obj_callback)
    runner = cli_runner.invoke(app, ["list"])
    assert runner.exit_code == 0


def test_tasks_with_daily_opts(cli_runner: CliRunner):
    app.callback()(get_fake_api_obj_callback)
    runner = cli_runner.invoke(app, ["list", "--daily"])
    assert runner.exit_code == 0


def test_tasks_with_weekly_opts(cli_runner: CliRunner):
    app.callback()(get_fake_api_obj_callback)
    runner = cli_runner.invoke(app, ["list", "--weekly"])
    assert runner.exit_code == 0
