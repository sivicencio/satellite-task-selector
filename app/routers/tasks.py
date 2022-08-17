from fastapi import APIRouter
from typing import List
from task_selector.handler import Handler
from task_selector.models import Task

router = APIRouter()

@router.post("/", tags=['tasks'])
async def select_tasks(tasks: List[Task]):
    selector_handler = Handler(tasks)
    selection_result = selector_handler.perform_selection()
    return selection_result
