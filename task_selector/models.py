from typing import List
from pydantic import BaseModel, NonNegativeFloat, constr

class Task(BaseModel):
    # pylint: disable=too-few-public-methods
    name: constr(min_length=1)
    resources: List[str] = []
    profit: NonNegativeFloat
