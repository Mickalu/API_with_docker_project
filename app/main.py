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
from info_data import information_data

app = FastAPI()
templates = Jinja2Templates(directory = "../templates")

data_info = information_data(DIR_PATH_DATA, FILE_DATA_CSV)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/algo")
def findAlgo():
    return displayBetterAlgo(DIR_PATH_DATA, FILE_DATA_CSV)

@app.get("/data")
def function_display_info_data():
    return data_info

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/html")
def html_file(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": 2})

@app.get("/html/data")
def html_file(request: Request):
    return templates.TemplateResponse("data_info.html", {"request": request, "data_info": data_info})

@app.get("/html/algo")
def html_file(request: Request):
    return templates.TemplateResponse("meilleur_algo.html", {"request": request, "tab_algo":  displayBetterAlgo(DIR_PATH_DATA, FILE_DATA_CSV)})