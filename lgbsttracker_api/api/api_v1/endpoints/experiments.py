from typing import List

from fastapi import APIRouter

from lgbsttracker import get_experiment_by_uuid
from lgbsttracker.entities import Experiment

router = APIRouter()


@router.get("/", response_model=List[Experiment])
async def read_experiments(uuid: str = "experiment1",):
    """
    Retrieve experiments.
    """
    experiments = await get_experiment_by_uuid(uuid)
    return experiments