from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI(title = "TODO API")
display = [1,2,3]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component : {}".format(component_id)}

@app.post("/package/{priority}")
async def make_package(priority: int, package: Package, value: bool):
    return {"priority": priority, **package.dict(), "value": value}


@app.post("/otherPackage/", response_model = Package, response_model_exclude_unset = True)#on va repondre ce model et pas le model In du coup et include exclude juste pour montrer ou non des choses
async def make_other_package(package: PackageIn): 
    return package