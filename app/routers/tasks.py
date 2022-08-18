from fastapi import APIRouter, status
from typing import Dict, List
from task_selector.handler import Handler
from task_selector.models import Task
from task_selector.storage import TaskStorage

router = APIRouter()

@router.post("/", tags=['tasks'], response_model=Dict[str, List[Task]])
async def select_tasks(tasks: List[Task]):
    selector_handler = Handler(tasks)
    selection_result = selector_handler.perform_selection()
    return selection_result

@router.get("/selected", tags=['tasks'], response_model=List[Task])
async def get_selected_tasks():
    storage = TaskStorage()
    return storage.get_selected_tasks()

@router.get("/standby", tags=['tasks'], response_model=List[Task])
async def get_standby_tasks():
    storage = TaskStorage()
    return storage.get_standby_tasks()

@router.delete("/selected", tags=['tasks'], status_code=status.HTTP_204_NO_CONTENT)
async def clear_selected_tasks():
    storage = TaskStorage()
    storage.clear_selected_tasks()

@router.delete("/standby", tags=['tasks'], status_code=status.HTTP_204_NO_CONTENT)
async def clear_standby_tasks():
    storage = TaskStorage()
    storage.clear_standby_tasks()
