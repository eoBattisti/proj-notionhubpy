from dataclasses import dataclass

from custom_dataclasses import BaseDataclass, BasePropertiesClass


@dataclass
class BirthdayProperties(BasePropertiesClass):
    data: str
    name: str

@dataclass
class BirthdayItem(BaseDataclass):

    def __post_init__(self) -> None:
        self.properties: BirthdayProperties = self._sanitize_properties_data(self.properties)

    def _sanitize_properties_data(self, data: dict) -> BirthdayProperties:
        name = data.get("Name", {}).get("title", [])
        if name:
            name = name[0].get("plain_text")

        data = data.get("Data", {}).get("rich_text", [])
        if data:
            data = data[0].get("plain_text")

        return BirthdayProperties(name=name, data=data)
