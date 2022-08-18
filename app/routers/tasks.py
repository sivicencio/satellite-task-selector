from fastapi import APIRouter
from typing import List
from task_selector.handler import Handler
from task_selector.models import Task
from task_selector.storage import TaskStorage

router = APIRouter()

@router.post("/", tags=['tasks'])
async def select_tasks(tasks: List[Task]):
    selector_handler = Handler(tasks)
    selection_result = selector_handler.perform_selection()
    return selection_result

@router.get("/selected", tags=['tasks'])
async def get_selected_tasks():
    storage = TaskStorage()
    return storage.get_selected_tasks()

@router.get("/standby", tags=['tasks'])
async def get_standby_tasks():
    storage = TaskStorage()
    return storage.get_standby_tasks()
