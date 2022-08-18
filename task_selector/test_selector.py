# pylint: disable=redefined-outer-name, unused-import

from .test.fixtures import (
    empty_tasks,
    valid_all_compatible_different_resources_tasks,
    valid_all_compatible_no_resources_tasks,
    valid_two_compatible_tasks_profit_incompatible,
    valid_two_compatible_tasks_profit_compatibles,
    valid_one_compatible_empty_resources_tasks,
    valid_all_incompatible_tasks
)
from .selector import select_tasks

def test_select_tasks_empty_list(empty_tasks):
    selected, not_selected = select_tasks(empty_tasks)
    assert len(selected) == 0
    assert len(not_selected) == 0

def test_select_tasks_valid_all_compatible_different_resources_tasks(
    valid_all_compatible_different_resources_tasks):
    selected, not_selected = select_tasks(valid_all_compatible_different_resources_tasks)
    assert len(selected) == len(valid_all_compatible_different_resources_tasks)
    assert len(not_selected) == 0

def test_select_tasks_valid_all_compatible_no_resources_tasks(
    valid_all_compatible_no_resources_tasks):
    selected, not_selected = select_tasks(valid_all_compatible_no_resources_tasks)
    assert len(selected) == len(valid_all_compatible_no_resources_tasks)
    assert len(not_selected) == 0


def test_select_tasks_valid_two_compatible_tasks_profit_incompatible(
    valid_two_compatible_tasks_profit_incompatible):
    selected, not_selected = select_tasks(valid_two_compatible_tasks_profit_incompatible)
    assert len(selected) == 1
    assert len(not_selected) == 2

def test_select_tasks_valid_two_compatible_tasks_profit_compatibles(
    valid_two_compatible_tasks_profit_compatibles):
    selected, not_selected = select_tasks(valid_two_compatible_tasks_profit_compatibles)
    assert len(selected) == 2
    assert len(not_selected) == 1

def test_select_tasks_valid_one_compatible_empty_resources_tasks(
    valid_one_compatible_empty_resources_tasks):
    selected, not_selected = select_tasks(valid_one_compatible_empty_resources_tasks)
    assert len(selected) == 2
    assert selected[0] == valid_one_compatible_empty_resources_tasks[0]
    assert selected[1] == valid_one_compatible_empty_resources_tasks[2]
    assert len(not_selected) == 2
    assert not_selected[0] == valid_one_compatible_empty_resources_tasks[1]
    assert not_selected[1] == valid_one_compatible_empty_resources_tasks[3]

def test_select_tasks_valid_all_incompatible_tasks(valid_all_incompatible_tasks):
    selected, not_selected = select_tasks(valid_all_incompatible_tasks)
    assert len(selected) == 1
    assert selected[0] == valid_all_incompatible_tasks[2]
    assert len(not_selected) == 2
    assert not_selected[0] == valid_all_incompatible_tasks[0]
    assert not_selected[1] == valid_all_incompatible_tasks[1]
