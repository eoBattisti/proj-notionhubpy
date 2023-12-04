import json
from datetime import datetime
from typing import List, Optional
import requests
from requests import Response

from cli.notion_api import NotionBaseAPI
from cli.commands.tasks.entities import TaskToCreate
from cli.settings import API_TOKEN, API_VERSION, TASKS_DABASE_ID, API_URL


class TasksNotionAPI(NotionBaseAPI):
    """A class for interacting with the Notion API to manage tasks database."""


    def __init__(self) -> None:
        super().__init__(api_token=API_TOKEN,
                         notion_version=API_VERSION,
                         database_id=TASKS_DABASE_ID)

    def query_tasks(self,
                    daily: bool = False,
                    weekly: bool = False) -> List[dict]:
        """
        List tasks based on the given filter.

        Parameters:
        - daily (bool): If True, filter tasks for the current day.
        - weekly (bool): If True, filter tasks for the current week.

        Returns:
        - List[TaskItem]: A list of TaskItem instances representing the queried tasks.

        """
        filter: Optional[dict] = {
            "filter": {
                "and": [
                    {
                        "property": "Feita",
                        "checkbox": {
                            "equals": False
                        }
                    },
                    {
                        "property": "Data",
                        "date": {}
                    }
                ]
            }
        }
        if daily:
            filter["filter"]["and"][1]["date"] = {"equals": datetime.today().date().isoformat()}
        elif weekly:
            filter["filter"]["and"][1]["date"] = {"this_week": {}}
        else:
            filter = {"filter": {"property": "Feita", "checkbox": {"equals": False}}} 
        response = requests.post(
            f"{API_URL}/databases/{self.database_id}/query",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Notion-Version": self.notion_version,
            },
            json=json.loads(json.dumps(filter))
        )
        return response.json()["results"]

    def create_tasks(self, task: TaskToCreate) -> Response:
        """Creates a inbox tasks into the Tasks Database"""
        response = requests.post(
            f"{API_URL}/pages",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Notion-Version": self.notion_version,
            },
            json=task.as_dict(),
        )
        return response
