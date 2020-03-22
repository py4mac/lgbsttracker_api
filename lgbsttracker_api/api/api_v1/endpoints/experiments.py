from typing import List

from fastapi import APIRouter, Response

from lgbsttracker import get_experiment_by_uuid
from lgbsttracker.entities import Experiment

router = APIRouter()


@router.get("/", response_model=List[Experiment])
async def read_experiments(response: Response, uuid: str = "experiment1"):
    """
    Retrieve experiments.
    """
    experiments = await get_experiment_by_uuid(uuid)
    response.headers["X-Total-Count"] = str(len(experiments))
    return experiments
