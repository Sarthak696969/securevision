from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db
from securevision.db.models import ModelDef

router = APIRouter()

class ModelIn(BaseModel):
    name: str
    arch: str
    task: str
    params: dict | None = {}

@router.post("/define")
def define(m: ModelIn, db: Session = Depends(get_db)):
    row = ModelDef(name=m.name, arch=m.arch, task=m.task, params_json="{}")
    db.add(row); db.commit(); db.refresh(row)
    return {"id": row.id}

@router.get("")
def list_models(db: Session = Depends(get_db)):
    return db.query(ModelDef).all()
