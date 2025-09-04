from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db

router = APIRouter()

class XAIIn(BaseModel):
    experiment_id: int
    sample_ids: list[int]
    xai: str

@router.post("/xai")
def run_xai(body: XAIIn, db: Session = Depends(get_db)):
    return {"job_id": 1, "xai": body.xai, "status": "queued"}
