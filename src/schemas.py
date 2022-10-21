from pydantic import BaseModel

class EyeColorBase(BaseModel):
    id: int
    color: str

    class Config:
        orm_mode = True

class CharacterBase(BaseModel):
    id: int
    name: str
    height: float 
    mass: float  
    eye_color: int

    class Config:
        orm_mode = True

class CharacterCreate(CharacterBase):
    hair_color: str
    skin_color: str

class Character(CharacterBase):
    pass


    