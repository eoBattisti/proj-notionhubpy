from dataclasses import dataclass

from cli.custom_dataclasses import BaseDataclass


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

