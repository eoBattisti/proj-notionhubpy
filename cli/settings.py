from pathlib import Path
import typer
import yaml



APP_NAME = "notionpy"

APP_DIR = typer.get_app_dir(APP_NAME)

config_path = Path(APP_DIR) / "settings.yaml"

API_URL = "https://api.notion.com/v1"
ACCEPTED_KEYS = ["id", "created_time", "archived", "properties", "url"]


parsed_yaml = None
if config_path.is_file():
    with open(config_path) as f:
        try:
            parsed_yaml = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            raise Exception("Could not load configuration file") from exc

TASKS_DABASE_ID: str = parsed_yaml["notion_api"]["task_database_id"]
BIRTHDAY_DATABASE_ID: str = parsed_yaml["notion_api"]["birthdays_database_id"]
PROJECTS_DATABSE_ID: str = parsed_yaml["notion_api"]["projects_database_id"]
API_TOKEN: str = parsed_yaml["notion_api"]["api_key"]
API_VERSION: str = str(parsed_yaml["notion_api"]["api_version"])