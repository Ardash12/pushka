import uvicorn
import sys

from fastapi import FastAPI

from app.categories import category_router
from app.items import item_router
from app.users import users_router


application = FastAPI()
application.include_router(category_router, prefix='/category', tags=['Category'])
application.include_router(item_router, prefix='/item', tags=['Item'])
application.include_router(users_router, prefix='/user', tags=['User'])

def main() -> None:
    uvicorn.run('main:application', host="127.0.0.1", port=8000, reload=True)
    
if __name__ == "__main__":
    main()
    