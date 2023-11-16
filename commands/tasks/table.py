from typing import List

from base_table import BaseTable

class TasksTable(BaseTable):
    
    def __init__(self, fields: List[str] = ["Name", "Date", "Done"]) -> None:
        super().__init__(fields)

