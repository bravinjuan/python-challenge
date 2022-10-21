from fastapi import APIRouter, status, Depends, HTTPException
from . import schemas, services
from .database import get_db
from sqlalchemy.orm import Session

character_router = APIRouter(prefix="/character", tags=["character"])

@character_router.get("/getAll", 
            response_model=list[schemas.Character],
            status_code=200,
            summary="Get all characters",
            description="Get a list of all characters")
def get_all_characters(db: Session = Depends(get_db)):
    characters = services.get_all_characters(db)
    return characters

@character_router.get("/get/{name}", 
            response_model=list[schemas.CharacterCreate],
            status_code=200,
            summary="Get characters",
            description="Get characters by name")
def get_character_by_name(name: str, db: Session = Depends(get_db)):
    characters = services.get_character_by_name(db, name)
    if characters is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return characters

@character_router.post("/add", 
            response_model=schemas.CharacterCreate,
            status_code=status.HTTP_201_CREATED,
            summary="Create an character",
            response_description="The created character",
            description="Create an character with all the information, id, name, height, mass, hair color, skin color and eye color",
            responses={400: {"description": "character id already registered"}})
def add_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    db_character = services.get_character_by_id(db, character.id)
    if db_character:
        raise HTTPException(status_code=400, detail="ID already registered")
    services.add_character(db, character)
    return character

@character_router.delete("/delete/{id}", 
                status_code=200,
                summary="Delete an character",
                description="Delete an character by id",
                responses={400: {"description": "character doesn't exist"}})
def delete_character(id: int, db: Session = Depends(get_db)):
    character = services.get_character_by_id(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return services.delete_character(db, id)


eye_router = APIRouter(prefix="/eye", tags=["eye"])

@eye_router.get("/getAll", 
            response_model=list[schemas.EyeColorBase],
            status_code=200,
            summary="Get all eye colors",
            description="Get a list of all eye colors")
def get_all_eye_colors(db: Session = Depends(get_db)):
    eye_colors = services.get_all_eye_colors(db)
    return eye_colors