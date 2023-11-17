from typing import List

from cli.base_table import BaseTable


class ProjectsTable(BaseTable):

    def __init__(self, fields: List[str] = ["Name", "Idate", "Edate", "Progress"]) -> None:
        super().__init__(fields)
