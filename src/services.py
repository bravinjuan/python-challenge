from fastapi import HTTPException
from . import app
from fastapi.encoders import jsonable_encoder

def get_all_items():
    return app.dictData

def get_item_by_name(name):
    items = list(filter(lambda x: x['name'] == name, app.dictData))
    return items

def add_item(item):
    items = list(filter(lambda x: x['id'] == item.id, app.dictData))
    if (items): 
        raise HTTPException(status_code=400, detail="Item id already registered")
    json_item = jsonable_encoder(item)
    app.dictData.append(json_item)
    return item

def delete_item(id):
    items = list(filter(lambda x: x['id'] == id, app.dictData))
    if (len(items) == 0):
        raise HTTPException(status_code=400, detail="Item doesn't exist")
    else:
        app.dictData = list(filter(lambda x: x['id'] != id, app.dictData))
        return "The item:{} has been deleted".format(id)