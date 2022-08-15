from typing import List
from pydantic import BaseModel

class Task(BaseModel):
    name: str
    resources: List[str] = []
    profit: int
