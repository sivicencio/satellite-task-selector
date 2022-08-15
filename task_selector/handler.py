from typing import List
from pydantic import parse_obj_as, ValidationError
from .models import Task
from .selector import select_tasks

class Handler:
    def __init__(self, tasks: List[Task] = []):
        self.tasks = self.build_and_validate(tasks)

    def build_and_validate(self, tasks: List[Task]) -> List[Task]:
        try:
            return parse_obj_as(List[Task], tasks)
        except ValidationError as e:
            print(e.errors())
            return []

    def perform_selection(self) -> List[Task]:
        return select_tasks(self.tasks)
