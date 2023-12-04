from typing import List
import requests

from cli.settings import API_URL

class NotionBaseAPI:
    """A generic class"""

    def __init__(self, api_token: str, notion_version: str, database_id: str) -> None:
        self.api_token: str = api_token
        self.notion_version: str = notion_version
        self.database_id: str = database_id

    def query(self) -> List[dict]:
        response = requests.post(
            f"{API_URL}/databases/{self.database_id}/query",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Notion-Version": self.notion_version,
            }
        )
        return response.json()["results"]
