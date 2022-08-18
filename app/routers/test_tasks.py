# pylint: disable=redefined-outer-name, unused-argument, unused-import

from fastapi.testclient import TestClient
from task_selector.test.fixtures import (
    mock_empty_storage,
    mock_non_empty_storage,
    valid_all_incompatible_tasks,
    invalid_tasks_empty_name,
    invalid_tasks_no_text_name,
    invalid_tasks_text_profit,
    invalid_tasks_negative_profit,
    invalid_tasks_text_resources
)
from ..main import app

client = TestClient(app)

def test_get_selected_tasks_empty(mock_empty_storage):
    response = client.get('/tasks/selected')
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_get_selected_tasks_non_empty(mock_non_empty_storage):
    response = client.get('/tasks/selected')
    assert response.status_code == 200
    assert len(response.json()) != 0

def test_get_standby_tasks_empty(mock_empty_storage):
    response = client.get('/tasks/standby')
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_get_standby_tasks_non_empty(mock_non_empty_storage):
    response = client.get('/tasks/standby')
    assert response.status_code == 200
    assert len(response.json()) != 0

def test_select_tasks_valid(mock_empty_storage, valid_all_incompatible_tasks):
    raw_list = list(map(lambda task: task.dict(), valid_all_incompatible_tasks))
    response = client.post(
        '/tasks/',
        json=raw_list
    )
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data['selected']) > 0
    assert len(response_data['not_selected']) > 0

def test_select_tasks_invalid_empty_name(mock_empty_storage, invalid_tasks_empty_name):
    response = client.post(
        '/tasks/',
        json=invalid_tasks_empty_name
    )
    assert response.status_code == 422

def test_select_tasks_invalid_no_text_name(mock_empty_storage, invalid_tasks_no_text_name):
    response = client.post(
        '/tasks/',
        json=invalid_tasks_no_text_name
    )
    assert response.status_code == 422

def test_select_tasks_invalid_text_profit(mock_empty_storage, invalid_tasks_text_profit):
    response = client.post(
        '/tasks/',
        json=invalid_tasks_text_profit
    )
    assert response.status_code == 422

def test_select_tasks_invalid_negative_profit(mock_empty_storage, invalid_tasks_negative_profit):
    response = client.post(
        '/tasks/',
        json=invalid_tasks_negative_profit
    )
    assert response.status_code == 422

def test_select_tasks_invalid_text_resources(mock_empty_storage, invalid_tasks_text_resources):
    response = client.post(
        '/tasks/',
        json=invalid_tasks_text_resources
    )
    assert response.status_code == 422
