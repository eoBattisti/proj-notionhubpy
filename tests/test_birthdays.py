import typer
from typer.testing import CliRunner
from typing import List

from .utils import generate_birthdays
from cli.commands.birthday.commands import app


class FakeBirthdayAPI():

    def query(self) -> List[dict]:
        return generate_birthdays()

def get_fake_api_obj_callback(ctx: typer.Context):
    ctx.obj = FakeBirthdayAPI()


def test_birthdays_list(cli_runner: CliRunner):
    app.callback()(get_fake_api_obj_callback)
    result = cli_runner.invoke(app, ["list"])
    assert result.exit_code == 0, result.output
