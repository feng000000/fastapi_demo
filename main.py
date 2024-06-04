from fastapi import FastAPI

from api import main_router
from api.item import item_router

app = FastAPI()

app.include_router(main_router, prefix="/api")
app.include_router(item_router, prefix="/api/item")

