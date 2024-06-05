# all pydantic models

from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

class Polymerization(BaseModel):
    item : Item1
    user : User