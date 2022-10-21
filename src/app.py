from fastapi import FastAPI
from .routes import character_router, eye_router
from . import models
from .database import engine
from sqlalchemy import text

models.Base.metadata.create_all(bind=engine)

with engine.connect() as con:
    with open("eye_colors.sql") as file:
        query = text(file.read())
        con.execute(query)

app = FastAPI()
app.include_router(character_router)
app.include_router(eye_router)
        
