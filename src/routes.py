from fastapi import APIRouter, status
from . import schemas
from . import services

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/getAll", 
            response_model=list[schemas.Item],
            status_code=200,
            summary="Get all items",
            description="Get a list of all items")
def get_all_items():
    items = services.get_all_items()
    return items

@router.get("/get/{name}", 
            response_model=list[schemas.ItemCreate],
            status_code=200,
            summary="Get items",
            description="Get items by name")
def get_item_by_name(name: str):
    items = services.get_item_by_name(name)
    return items

@router.post("/add", 
            response_model=schemas.ItemCreate,
            status_code=status.HTTP_201_CREATED,
            summary="Create an item",
            response_description="The created item",
            description="Create an item with all the information, id, name, height, mass, hair color, skin color and eye color",
            responses={400: {"description": "Item id already registered"}})
def add_item(item: schemas.ItemCreate):
    services.add_item(item)
    return item

@router.delete("/delete/{id}", 
                status_code=200,
                summary="Delete an item",
                description="Delete an item by id",
                responses={400: {"description": "Item doesn't exist"}})
def delete_item(id: int):
    return services.delete_item(id)
