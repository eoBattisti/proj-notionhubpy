from typing import List
from rich.table import Table


class BaseTable(Table):

    def __init__(self, fields: List[str], data: List[dict]) -> None:
        """Generates a rich table based on a list of fields"""
        super().__init__()
        self.fields: List[str] = fields
        self.data = self._sanitize_data(data)
        for field in fields:
            self.add_column(field)

    def _sanitize_data(self, data: List[dict]) -> List[dict]:
        filtered_data = []

        for item in data:
            obj = {}
            for field in self.fields:
                if field in item["properties"]:
                    ftype = item["properties"][field]["type"]
                    value = item["properties"][field][ftype]

                    if ftype in ["title", "text", "rich_text"] and isinstance(value, list):
                        value = value[0]["text"]["content"] 
                    elif ftype == "rollup" and isinstance(value, dict):
                        value = value["number"]
                        if value:
                            value = round(value * 100, 2)
                        else:
                            value = 0
                    elif ftype == "date" and isinstance(value, dict):
                        value = value["start"]

                    if value is None:
                        value = "-"

                    obj[field] = str(value)
            filtered_data.append(obj)

        return filtered_data

    def fill_table(self):
        """Fill table with the given objects"""
        for obj in self.data:
            self.add_row(*obj.values())
