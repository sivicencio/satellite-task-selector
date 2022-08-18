import os
from typing import List
import redis
from .models import Task

KEYS = {
    'selected': 'tasks:selected',
    'standby': 'tasks:standby'
}

MAX_ITEMS = {
    'selected': 100,
    'standby': 100
}

class TaskStorage:
    def __init__(self):
        redis_url = os.getenv('REDIS_URL', 'redis://localhost')
        self.storage = redis.Redis.from_url(redis_url, decode_responses=True)

    def get_standby_tasks(self) -> List[Task]:
        return self.__get_tasks(KEYS['standby'])

    def add_standby_tasks(self, tasks: List[Task]) -> int:
        return self.__add_tasks(tasks, KEYS['standby'], MAX_ITEMS['standby'])

    def clear_standby_tasks(self) -> bool:
        return self.__clear_tasks(KEYS['standby'])

    def get_selected_tasks(self) -> List[Task]:
        return self.__get_tasks(KEYS['selected'])

    def add_selected_tasks(self, tasks: List[Task]) -> int:
        return self.__add_tasks(tasks, KEYS['selected'], MAX_ITEMS['selected'])

    def clear_selected_tasks(self) -> bool:
        return self.__clear_tasks(KEYS['selected'])

    def __get_tasks(self, key: str) -> List[Task]:
        tasks_in_json = self.storage.lrange(key, 0, -1)
        return list(map(Task.parse_raw, tasks_in_json))

    def __add_tasks(self, tasks: List[Task], key: str, max_items: int) -> int:
        for task in tasks:
            self.storage.lpush(key, task.json())
        self.storage.ltrim(key, 0, max_items - 1)
        return len(tasks)

    def __clear_tasks(self, key: str) -> bool:
        deleted_keys_count = self.storage.delete(key)
        return deleted_keys_count in [0, 1]
