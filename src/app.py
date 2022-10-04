from unicodedata import name
from fastapi import Depends, FastAPI, HTTPException
import json
from . import routes

app = FastAPI()
app.include_router(routes.router)

with open('./data.json') as d:
    dictData = json.load(d)

