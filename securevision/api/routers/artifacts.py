from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from securevision.api.deps import get_db
from securevision.db.models import Artifact

router = APIRouter()

@router.get("/{experiment_id}/artifacts")
def list_artifacts(experiment_id: int, db: Session = Depends(get_db)):
    return db.query(Artifact).filter(Artifact.experiment_id==experiment_id).all()
