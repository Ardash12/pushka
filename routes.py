from fastapi import APIRouter
# from reference.reference_stat import router
from reference import reference_stat


routes = APIRouter()

routes.include_router(reference_stat.router, prefix='/reference')
