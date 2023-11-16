from typing import List
from rich.table import Table

class BaseTable(Table):

    def __init__(self, fields: List[str] = []) -> None:
        """Generates a rich table based on a list of fields"""
        super().__init__()
        self.fields: List[str] = fields
        for field in fields:
            self.add_column(field)

    def fill_table(self, objects):
        """Fill table with the given objects"""
        for obj in objects:
            values = [getattr(obj.properties, field.lower()) for field in self.fields]
            self.add_row(*[str(value) for value in values])
