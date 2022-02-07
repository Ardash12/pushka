from fastapi import APIRouter
from reference.reference_stat import router


routes = APIRouter()

routes.include_router(router, prefix='/reference')
