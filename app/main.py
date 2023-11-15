from fastapi import FastAPI
from starlette import status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.schemas import Item
from . import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    path="/",
    response_model=Item,
    status_code=status.HTTP_200_OK,
)
async def root():
    return {"message": "Hello World"}
