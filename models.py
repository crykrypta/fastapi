from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name: str
    age: int
    is_adult: Union[bool, None] = None


