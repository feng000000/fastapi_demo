from fastapi import FastAPI

from controller.auth import auth_router
from controller.item import item_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth")
app.include_router(item_router, prefix="/api/item")
