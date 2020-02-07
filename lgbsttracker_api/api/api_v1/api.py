from fastapi import APIRouter

from lgbsttracker_api.api.api_v1.endpoints import experiments

api_router = APIRouter()
api_router.include_router(experiments.router, prefix="/experiments", tags=["experiments"])