from fastapi import APIRouter

auth_router = APIRouter()


from .login import *  # noqa: E402 F403
