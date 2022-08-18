import logging
import time
from typing import List, Set, Tuple
from .models import Task

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def select_tasks(tasks: List[Task]) -> Tuple[List[Task], List[Task]]:
    # pylint: disable=too-many-locals, too-many-branches
    logging.info('Selecting higher profit tasks from %s tasks', len(tasks))
    start_time = time.time()

    # Step 1: Group tasks based on resources compatibility

    # Keep a mapping between resources and tasks requiring them
    resources_to_tasks = {}
    for index, task in enumerate(tasks):
        for resource in task.resources:
            resource_required_by = resources_to_tasks.get(resource) or []
            resource_required_by.append(index)
            resources_to_tasks[resource] = resource_required_by

    incompatible_tasks_already_grouped: Set[int] = set()
    full_compatible_tasks_indices: Set[int] = set()
    groups: List[Set[int]] = []

    for index, task in enumerate(tasks):
        if len(task.resources) == 0:
            full_compatible_tasks_indices.add(index)
            continue

        incompatible_indexed_tasks: Set[int] = set()
        for resource in task.resources:
            resource_required_by = resources_to_tasks.get(resource)
            for requirer_index in resource_required_by:
                if requirer_index != index:
                    incompatible_indexed_tasks.add(requirer_index)

        if len(incompatible_indexed_tasks) == 0:
            full_compatible_tasks_indices.add(index)
            continue

        group: Set[int] = set()
        for j, task in enumerate(tasks):
            if j not in incompatible_indexed_tasks and j not in incompatible_tasks_already_grouped:
                group.add(j)
                incompatible_tasks_already_grouped.add(j)
        if len(group) > 0:
            groups.append(group)

    # No groups so far means all tasks are compatible so add it as a group
    if len(groups) == 0:
        groups.append(full_compatible_tasks_indices)

    # Step 2: Select group with higher profit

    max_profit = 0
    selected_group_index = 0
    for i, _ in enumerate(groups):
        # Add tasks compatible with every other (full compatible) to each group
        groups[i] = groups[i] | full_compatible_tasks_indices
        group_profit = 0
        for j in groups[i]:
            group_profit += tasks[j].profit
        if group_profit > max_profit:
            max_profit = group_profit
            selected_group_index = i

    # Step 3: Return both the group with higher profit and the rest

    selected_tasks = []
    not_selected_tasks = []
    for i, _ in enumerate(groups):
        # Remove full compatible tasks from not selected groups
        if i != selected_group_index:
            groups[i] = groups[i] - full_compatible_tasks_indices
        for j in groups[i]:
            assigned_tasks = selected_tasks if i == selected_group_index else not_selected_tasks
            assigned_tasks.append(tasks[j])

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info('Execution time: %s seconds', elapsed_time)
    logging.info('Result: %s tasks selected and %s not selected',
        len(selected_tasks), len(not_selected_tasks))

    return selected_tasks, not_selected_tasks
