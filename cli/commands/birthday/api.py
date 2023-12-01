from cli.notion_api import NotionBaseAPI
from cli.settings import API_VERSION, API_TOKEN, BIRTHDAY_DATABASE_ID


class BirthdayNotionAPI(NotionBaseAPI):
    """A class for interacting with the Notion API to manage tasks database."""


    def __init__(self) -> None:
        super().__init__(api_token=API_TOKEN,
                         notion_version=API_VERSION,
                         database_id=BIRTHDAY_DATABASE_ID)

