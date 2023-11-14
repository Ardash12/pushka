from fastapi import FastAPI
from starlette import status

from app.schemas import Item

app = FastAPI()


@app.get(
    path="/",
    response_model=Item,
    status_code=status.HTTP_200_OK,
)
async def root():
    return {"message": "Hello World"}
