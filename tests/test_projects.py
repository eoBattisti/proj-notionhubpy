import typer
from typer.testing import CliRunner

from .utils import generate_projects
from cli.commands.projects.commands import app

class FakeProjectAPI:

    def query(self):
        return generate_projects()

def get_fake_api_obj_callback(ctx: typer.Context):
    ctx.obj = FakeProjectAPI()

def test_projects_list(cli_runner: CliRunner):
    app.callback()(get_fake_api_obj_callback)
    result = cli_runner.invoke(app, ["list"])
    print(result.output)
    assert result.exit_code == 0
