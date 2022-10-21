from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class EyeColor(Base):
    __tablename__ = "eye_colors"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String(50), index=True)

    character = relationship("Character")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(Integer,ForeignKey("eye_colors.id"))
