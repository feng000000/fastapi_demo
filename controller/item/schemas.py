# all pydantic models

from pydantic import BaseModel
from pydantic import HttpUrl


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


class User(BaseModel):
    username: str
    full_name: str | None = None


class Polymerization(BaseModel):
    item: Item1
    user: User


class Image(BaseModel):
    url: HttpUrl
    name: str


class ManyImages(BaseModel):
    name: str
    tags: set[str] = set()
    images: list[Image] | None = None
