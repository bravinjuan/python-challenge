from . import models
from sqlalchemy.orm import Session

def get_all_characters(db: Session):
    return db.query(models.Character).order_by(models.Character.id).all()

def get_all_eye_colors(db: Session):
    return db.query(models.EyeColor).order_by(models.EyeColor.id).all()

def get_character_by_id(db: Session, id):
    character = db.query(models.Character).filter(models.Character.id == id).all()
    return character

def get_character_by_name(db: Session, name):
    characters = db.query(models.Character).filter(models.Character.name == name).all()
    return characters

def add_character(db: Session, character):
    db_character = models.Character(
        id = character.id, 
        name = character.name, 
        height = character.height,
        mass = character.mass,
        hair_color = character.hair_color,
        skin_color = character.skin_color,
        eye_color = character.eye_color)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return character

def delete_character(db: Session, id):
    db.query(models.Character).filter(models.Character.id == id).delete()
    db.commit()
    return "The character:{} has been deleted".format(id)