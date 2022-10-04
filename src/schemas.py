from uuid import UUID
from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    name: str
    height: float 
    mass: float  

class ItemCreate(ItemBase):
    hair_color: str
    skin_color: str
    eye_color: str

class Item(ItemBase):
    pass

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True