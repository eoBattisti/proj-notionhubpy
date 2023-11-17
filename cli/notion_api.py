from typing import List
import requests

from cli.settings import API_URL, ACCEPTED_KEYS

class NotionBaseAPI:
    """A generic class"""

    def __init__(self, api_token: str, notion_version: str, database_id: str) -> None:
        self.api_token: str = api_token
        self.notion_version: str = notion_version
        self.database_id: str = database_id

    def _sanitize_data(self, data: List[dict]) -> List[dict]:
        items = []
        for i in data:
            temp = {k: v for k, v in i.items() if k in ACCEPTED_KEYS}
            items.append(temp)
        return items

    def query(self) -> List[dict]:
        response = requests.post(
            f"{API_URL}/databases/{self.database_id}/query",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Notion-Version": self.notion_version,
            }
        )
        items = self._sanitize_data(data=response.json()["results"])
        return items
