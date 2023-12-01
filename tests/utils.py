import random
import uuid
from datetime import datetime
from typing import List


def generate_tasks() -> List[dict]:
    tasks = []
    for _ in range(10):
        data = {
            'id': f"{uuid.uuid4()}",
            'created_time': datetime(2023, 12, 1),
            'archived': random.choice([True, False]),
            'properties': {
                'Data': {'id': f'{uuid.uuid4()}', 'type': 'date', 'date': datetime(2023, 12, 1)},
                'Descrição': {'id': f'{uuid.uuid4()}', 'type': 'rich_text', 'rich_text': []},
                'Recursos': {'id': f'{uuid.uuid4()}', 'type': 'relation', 'relation': [], 'has_more': False},
                'Feita': {'id': f'{uuid.uuid4()}', 'type': 'checkbox', 'checkbox': False},
                'Projetos': {'id': f'{uuid.uuid4()}', 'type': 'relation', 'relation': [], 'has_more': False},
                'Notas': {'id': f'{uuid.uuid4()}', 'type': 'relation', 'relation': [], 'has_more': False},
                'URL': {'id': f'{uuid.uuid4()}', 'type': 'url', 'url': None},
                'Name': {
                    'id': 'title',
                    'type': 'title',
                    'title': [{'type': 'text', 'text': {'content': 'Pytest Test Task', 'link': None},
                                'annotations': {'bold': False, 'italic': False, 'strikethrough': False,
                                                'underline': False, 'code': False, 'color': 'default'},
                                'plain_text': 'Pytest Test Task', 'href': None}]
                }},
            'url': 'http://foobar.com'
        }
        tasks.append(data)
    return tasks

def generate_birthdays() -> List[dict]:
    birthdays = []
    for _ in range(10):
        data = {
            'id': f'{uuid.uuid4()}',
            'created_time': datetime(2023, 12, 1),
            'archived': random.choice([True, False]),
            'properties': {
                'Data': {
                    'id': f'{uuid.uuid4()}',
                    'type': 'rich_text', 
                    'rich_text': [{
                        'type': 'text',
                        'text': {
                            'content': '01/01',
                        },
                        'plain_text': '01/01',
                    }]
                },
                'icons': {
                    'id': f'{uuid.uuid4()}',
                    'type': 'rich_text',
                    'rich_text': [{
                        'type': 'text',
                        'text': {
                            'content': '👩🏽',
                            'link': None
                        },
                        'plain_text': '👩🏽',
                    }]
                },
                'Name': {
                    'id': 'title',
                    'type': 'title',
                    'title': [{
                        'type': 'text',
                        'text': {'content': 'Foo Bar', 'link': None},
                        'plain_text': 'Foo Bar', 'href': None}]}}, 'url': ''}

        birthdays.append(data)
    return birthdays

def generate_projects() -> List[dict]:
    projects = []
    for _ in range(10):
        data = {
            'id': f'{uuid.uuid4()}',
            'created_time': datetime(2023, 12, 1),
            'archived': random.choice([True, False]),
            'properties': {
                'Progresso': {
                    'id': f'{uuid.uuid4()}',
                    'type': 'rollup',
                    'rollup': {
                        'type': 'number',
                        'number': None,
                        'function': 'percent_checked'
                    }
                },
                'Arquivado': {'id': 'RyyD', 'type': 'checkbox', 'checkbox': False},
                'Data final': {'id': '%60U%3Cs', 'type': 'date', 'date': None},
                'Data de inicio': {'id': 'waFk', 'type': 'date', 'date': None},
                'Name': {
                    'id': 'title',
                    'type': 'title',
                    'title': [{'type': 'text', 'text': {'content': 'Foo bar', 'link': None},
                               'plain_text': 'Faculdade Meliês', 'href': None}] }},
                    'url': 'http://foobar.com'
        }

        projects.append(data)
    return projects

