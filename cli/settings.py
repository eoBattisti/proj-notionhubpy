from pathlib import Path
import typer
import yaml



APP_NAME = "nthub"

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

TASKS_SETTINGS: dict = parsed_yaml["notion_api"]["databases"]["tasks"]
TASKS_DABASE_ID: str = TASKS_SETTINGS.get('id', '')
TASKS_FIELDS: list = TASKS_SETTINGS.get('fields', [])

BIRTHDAYS_SETTINGS: dict = parsed_yaml["notion_api"]["databases"]["birthdays"]
BIRTHDAY_DATABASE_ID: str = BIRTHDAYS_SETTINGS.get('id', '')
BIRTHDAY_FIELDS: list = BIRTHDAYS_SETTINGS.get('fields', [])

PROJECTS_SETTINGS: dict = parsed_yaml["notion_api"]["databases"]["projects"]
PROJECTS_DATABSE_ID: str = PROJECTS_SETTINGS.get('id', '')
PROJECTS_FIELDS: list = PROJECTS_SETTINGS.get('fields', [])

API_TOKEN: str = parsed_yaml["notion_api"]["api_key"]
API_VERSION: str = str(parsed_yaml["notion_api"]["api_version"])

