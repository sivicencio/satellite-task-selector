from typing import List, Dict
from pydantic import parse_obj_as, ValidationError
from .models import Task
from .selector import select_tasks
from .storage import TaskStorage

class Handler:
    def __init__(self, tasks: List[Task] = []):
        self.tasks = self.build_and_validate(tasks)
        self.storage = TaskStorage()

    def build_and_validate(self, tasks: List[Task]) -> List[Task]:
        try:
            return parse_obj_as(List[Task], tasks)
        except ValidationError as e:
            print(e.errors())
            return []

    def perform_selection(self) -> Dict[str, List[Task]]:
        standby_tasks = self.storage.get_standby_tasks()

        # Perform selection between standby tasks and received tasks
        joined_tasks = [*standby_tasks, *self.tasks]
        selected, not_selected = select_tasks(joined_tasks)

        # Clear standby tasks since selection was successful
        self.storage.clear_standby_tasks()

        # Persist new standby (not selected) tasks
        if len(not_selected) > 0:
            self.storage.add_standby_tasks(not_selected)

        # Persist selected tasks
        if len(selected) > 0:
            self.storage.add_selected_tasks(selected)

        return {
            'selected': selected,
            'not_selected': not_selected
        }
