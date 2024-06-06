from typing import Annotated
from typing import Optional
from fastapi import Path
from fastapi import Query
from fastapi import Depends
from fastapi import Header
from fastapi import Body
from fastapi import HTTPException

from controller.item import item_router
from controller.item.schemas import User
from controller.item.schemas import Polymerization


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
    return {
        "item_id": item_id,
        "q": q,
        "short": short,
        "count": count,
        "offset": offset,
    }


# polymerization pydantic model
@item_router.put("/items1/{item_id}")
async def update_item1(item_id: int, polymerization: Polymerization):
    results = {"item_id": item_id, "polymerization": polymerization}
    return results


# get_current_user denpendency
from fastapi.security import OAuth2PasswordBearer  # noqa: E402

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token", scheme_name="item_test_scheme"
)


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe",
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@item_router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


# dependencies in path operation


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Body(embed=True)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@item_router.get(
    "/items8/", dependencies=[Depends(verify_token), Depends(verify_key)]
)
async def read_items8():
    return [{"item": "Foo"}, {"item": "Bar"}]
