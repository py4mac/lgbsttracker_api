from typing import List

from fastapi import APIRouter, Response

from lgbsttracker import get_experiment_by_uuid, create_experiment
from lgbsttracker.entities import Experiment, ExperimentCreate

router = APIRouter()


@router.get("/", response_model=List[Experiment])
async def get_experiments(response: Response, uuid: str = "experiment1"):
    """
    Retrieve experiments.
    """
    experiments = await get_experiment_by_uuid(uuid)
    response.headers["X-Total-Count"] = str(len(experiments))
    return experiments


@router.post("/", response_model=Experiment)
async def post_experiment(experiment: ExperimentCreate):
    """
    Create a new experiment.
    """
    new_experiment = await create_experiment(experiment)
    return new_experiment
