from typing import List
from pydantic import BaseModel, NonNegativeFloat, constr

class Task(BaseModel):
    name: constr(min_length=1)
    resources: List[str] = []
    profit: NonNegativeFloat
