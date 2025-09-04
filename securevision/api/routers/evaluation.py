from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db

router = APIRouter()

class EvalIn(BaseModel):
    experiment_id: int
    eval_config: dict

@router.post("/evaluate")
def launch_eval(body: EvalIn, db: Session = Depends(get_db)):
    return {"job_id": 1, "status": "queued"}
