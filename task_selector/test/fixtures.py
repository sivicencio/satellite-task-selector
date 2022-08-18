# pylint: disable=unused-argument

import json
import os
from typing import Dict, List
from pydantic import parse_obj_as
import pytest
from ..models import Task
from ..storage import TaskStorage

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.json')
with open(filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

@pytest.fixture
def empty_tasks():
    return get_data_by_key('empty')

@pytest.fixture
def valid_all_compatible_different_resources_tasks() -> List[Task]:
    return get_data_by_key('valid_all_compatible_different_resources_tasks')

@pytest.fixture
def valid_all_compatible_no_resources_tasks() -> List[Task]:
    return get_data_by_key('valid_all_compatible_no_resources_tasks')

@pytest.fixture
def valid_two_compatible_tasks_profit_incompatible() -> List[Task]:
    return get_data_by_key('valid_two_compatible_tasks_profit_incompatible')

@pytest.fixture
def valid_two_compatible_tasks_profit_compatibles() -> List[Task]:
    return get_data_by_key('valid_two_compatible_tasks_profit_compatibles')

@pytest.fixture
def valid_one_compatible_empty_resources_tasks() -> List[Task]:
    return get_data_by_key('valid_one_compatible_empty_resources_tasks')

@pytest.fixture
def valid_all_incompatible_tasks() -> List[Task]:
    return get_data_by_key('valid_all_incompatible_tasks')

@pytest.fixture
def invalid_tasks_empty_name() -> List[Task]:
    return get_raw_data_by_key('invalid_tasks_empty_name')

@pytest.fixture
def invalid_tasks_no_text_name() -> List[Task]:
    return get_raw_data_by_key('invalid_tasks_no_text_name')

@pytest.fixture
def invalid_tasks_text_profit() -> List[Task]:
    return get_raw_data_by_key('invalid_tasks_text_profit')

@pytest.fixture
def invalid_tasks_negative_profit() -> List[Task]:
    return get_raw_data_by_key('invalid_tasks_negative_profit')

@pytest.fixture
def invalid_tasks_text_resources() -> List[Task]:
    return get_raw_data_by_key('invalid_tasks_text_resources')

@pytest.fixture
def mock_empty_storage(monkeypatch):
    def mock_get_selected_tasks(*args, **kwargs):
        return []

    def mock_get_standby_tasks(*args, **kwargs):
        return []

    def mock_add_selected_tasks(*args, **kwargs):
        return 1

    def mock_add_standby_tasks(*args, **kwargs):
        return 1

    def mock_clear_standby_tasks(*args, **kwargs):
        return True

    monkeypatch.setattr(TaskStorage, 'get_selected_tasks', mock_get_selected_tasks)
    monkeypatch.setattr(TaskStorage, 'get_standby_tasks', mock_get_standby_tasks)
    monkeypatch.setattr(TaskStorage, 'add_selected_tasks', mock_add_selected_tasks)
    monkeypatch.setattr(TaskStorage, 'add_standby_tasks', mock_add_standby_tasks)
    monkeypatch.setattr(TaskStorage, 'clear_standby_tasks', mock_clear_standby_tasks)

@pytest.fixture
def mock_non_empty_storage(monkeypatch):
    task = {
        'name': 'capture for client 1098',
        'resources': ['camera', 'disk', 'proc'],
        'profit': 9.2
    }
    def mock_get_selected_tasks(*args, **kwargs):
        return [task]

    def mock_get_standby_tasks(*args, **kwargs):
        return [task]

    monkeypatch.setattr(TaskStorage, 'get_selected_tasks', mock_get_selected_tasks)
    monkeypatch.setattr(TaskStorage, 'get_standby_tasks', mock_get_standby_tasks)

def get_raw_data_by_key(key: str) -> List[Dict]:
    return data[key]

def get_data_by_key(key: str) -> List[Task]:
    tasks_data = data[key]
    return convert_to_tasks(tasks_data)

def convert_to_tasks(tasks: List[Dict]) -> List[Task]:
    return parse_obj_as(List[Task], tasks)
