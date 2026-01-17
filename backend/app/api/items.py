from fastapi import APIRouter

router = APIRouter()
ITEMS = []

@router.post("/")
def create_item(item: dict):
    ITEMS.append(item)
    return item

@router.get("/")
def list_items():
    return ITEMS
