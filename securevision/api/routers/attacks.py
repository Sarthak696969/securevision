from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db

router = APIRouter()

class AttackIn(BaseModel):
    experiment_id: int | None = None
    model_artifact_id: int | None = None
    attack: str
    params: dict | None = {}

@router.post("/attack")
def launch_attack(body: AttackIn, db: Session = Depends(get_db)):
    # Enqueue Celery task in real system. Here we return stub response.
    return {"job_id": 1, "attack": body.attack, "status": "queued"}
