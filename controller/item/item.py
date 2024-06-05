from typing import Annotated
from typing import Optional
from fastapi import APIRouter
from fastapi import Path
from fastapi import Query

from view.item.schema import Item1
from view.item.schema import User
from view.item.schema import Polymerization

item_router = APIRouter()

@item_router.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@item_router.get("/items7/")
async def read_item7(
    item_id: int, 
    offset: Annotated[Optional[int], ("Offset for pagination")],
    q: Optional[str] = None, 
    short: bool = False, 
    count: int = 10, 
):
    return {"item_id": item_id, "q": q, "short": short, "count": count, "offset": offset}



@item_router.put("/items/{item_id}")
async def update_item(item_id: int, itemee: Item1, useree: User):
    results = {"item_id": item_id, "item": itemee, "user": useree}
    return results


@item_router.put("/items1/{item_id}")
async def update_item1(item_id: int, polymerization: Polymerization):
    results = {"item_id": item_id, "polymerization": polymerization}
    return results
