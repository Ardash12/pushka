from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import sqlalchemy   # работа с SQL https://habr.com/ru/post/513328/

from schemas import Reference


app = FastAPI()
# app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/items/{item_id}')
def items(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {'name': item.name, 'price': item.price, 'item_id': item_id, 'is': item.is_offer}


@app.post('/reference_stat')
def reference_stat(item: Reference):
    return item
