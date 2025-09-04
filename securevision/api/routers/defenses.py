from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db

router = APIRouter()

class DefenseIn(BaseModel):
    experiment_id: int
    defense: str
    params: dict | None = {}

@router.post("/defend")
def launch_defense(body: DefenseIn, db: Session = Depends(get_db)):
    return {"job_id": 1, "defense": body.defense, "status": "queued"}
