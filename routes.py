from fastapi import APIRouter
from reference import reference_stat


routes = APIRouter()

routes.include_router(reference_stat.router, prefix='/reference')
