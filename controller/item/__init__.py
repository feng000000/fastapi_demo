from fastapi import APIRouter

item_router = APIRouter()

from .item import *  # noqa: E402 F403
