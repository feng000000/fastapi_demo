from fastapi import APIRouter

main_router = APIRouter()

@main_router.get("/")
def read_root():
    return {"Hello": "World"}
