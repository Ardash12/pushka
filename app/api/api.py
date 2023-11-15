from fastapi import FastAPI

from routers import category_router


app = FastAPI

app.include_router(category_router, prefix='/category')
