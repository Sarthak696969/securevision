from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db

router = APIRouter()

class FedIn(BaseModel):
    base_experiment_id: int
    num_clients: int
    malicious_frac: float
    aggregator: str
    rounds: int = 1
    attack_pattern: dict | None = None

@router.post("/run")
def run_federated(body: FedIn, db: Session = Depends(get_db)):
    return {"run_id": 1, "status": "queued"}

@router.get("/{run_id}")
def get_run(run_id: int, db: Session = Depends(get_db)):
    return {"run_id": run_id, "status": "queued"}
