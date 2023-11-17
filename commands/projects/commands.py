import typer
from rich.console import Console

from notion_api import NotionAPI
from settings import API_TOKEN, API_VERSION, PROJECTS_DATABSE_ID
from commands.projects.table import ProjectsTable

app = typer.Typer()
notion_api = NotionAPI(api_token=API_TOKEN, notion_version=API_VERSION)

@app.command()
def list():
    """List all projects"""
    projects = notion_api.query_projects(database_id=PROJECTS_DATABSE_ID)
    table = ProjectsTable()
    table.fill_table(objects=projects)
    console = Console()
    console.print(table)
