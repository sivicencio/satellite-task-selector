import json
import os
from typing import Dict, List
from pydantic import parse_obj_as
import pytest
from ..models import Task

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

def get_data_by_key(key: str) -> List[Task]:
    tasks_data = data[key]
    return convert_to_tasks(tasks_data)

def convert_to_tasks(tasks: List[Dict]) -> List[Task]:
    return parse_obj_as(List[Task], tasks)
