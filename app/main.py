import uvicorn

from fastapi import APIRouter, FastAPI

# from .core.router import api_router
from categories import category_router


app = FastAPI()
app.include_router(category_router, prefix='/category')

def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
if __name__ == "__main__":
    main()
    