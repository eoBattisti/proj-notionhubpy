from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from custom_dataclasses import BaseDataclass, BasePropertiesClass

@dataclass
class ProjectsProperties(BasePropertiesClass):
    name: str
    idate: Optional[datetime]
    edate: Optional[datetime]
    progress: Optional[float]


@dataclass
class ProjectsItem(BaseDataclass):

    def __post_init__(self) -> None:
        self.properties: ProjectsProperties = self._sanitize_properties_data(data=self.properties)

    def _sanitize_properties_data(self, data: dict) -> ProjectsProperties:
        name: str = data.get("Name", {}).get("title", [])

        if name:
            name: str = name[0].get("plain_text", "")

        initial_date: Optional[datetime] = data.get("Data de inicio", {}).get("date", None)
        if isinstance(initial_date, dict):
            initial_date = initial_date.get("start")

        end_date: Optional[datetime] = data.get("Data final", {}).get("date", None)
        if isinstance(end_date, dict):
            end_date = end_date.get("start")

        progress: Optional[float] = data.get("Progresso", {}).get("rollup", {}).get("number", None)

        return ProjectsProperties(name=name, idate=initial_date,
                                  edate=end_date, progress=progress)
