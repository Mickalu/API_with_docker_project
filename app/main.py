import sys
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

FUNC_DIRECT = '../function_detection'
DIR_PATH_DATA = "../data"
FILE_DATA_CSV = "/KDD_clean_database.csv"

sys.path.insert(1,FUNC_DIRECT)
from trouver_meilleur_algo import displayBetterAlgo

app = FastAPI()
templates = Jinja2Templates(directory = "../templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/algo")
def findAlgo():
    return displayBetterAlgo(DIR_PATH_DATA, FILE_DATA_CSV)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/html")
def html_file(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 2})