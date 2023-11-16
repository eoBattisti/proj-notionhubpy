from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from custom_dataclasses import BaseDataclass, BasePropertiesClass


@dataclass
class TaskProperties(BasePropertiesClass):
    name: str
    done: bool 
    date: Optional[datetime] = None
    description: Optional[str] = None
    url: Optional[str] = None


@dataclass
class TaskItem(BaseDataclass):

    def __post_init__(self) -> None:
        self.properties: TaskProperties = self._sanitize_properties_data(data=self.properties) 

    def __str__(self) -> str:
        return f"{self.properties.name} - {self.properties.date} - {self.properties.done}"

    def _sanitize_properties_data(self, data: dict) -> BasePropertiesClass:
        name = data.get("Name", {}).get("title", [])
        if name:
            name = name[0].get("plain_text")

        date = data.get("Data", {}).get("date", "")
        if isinstance(date, dict):
            date = date.get("start")
        description = data.get("Description", {}).get("rich_text", [])
        done = data.get("Feita", {}).get("checkbox", False)
        url = data.get("URL", {}).get("url", "")
        return TaskProperties(name=name, date=date, description=description, done=done, url=url)


@dataclass
class TaskToCreate(BaseDataclass):
    database_id: str = ""
    title: str = ""

    def as_dict(self):
        data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Name": {"title": [{"text": {"content": self.title}}]},
            },
            "icon": {
                "type": "external",
                "external": {
                    "url": "https://www.notion.so/icons/checkmark_lightgray.svg"
                }
            }
        }
        return data
