from typing import List
from .models import Task

def select_tasks(tasks: List[Task]) -> List[Task]:
    print(f'Selecting higher profit tasks from {len(tasks)} tasks')
    # TODO: actual selection algorithm
    return tasks
