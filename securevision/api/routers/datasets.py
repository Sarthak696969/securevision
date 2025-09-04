from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from securevision.api.deps import get_db
from securevision.db.models import Dataset
from pathlib import Path
import subprocess, json

router = APIRouter()

class DatasetIn(BaseModel):
    name: str
    type: str
    version: str
    source_url: str | None = None

@router.post("/register")
def register(ds: DatasetIn, db: Session = Depends(get_db)):
    # Call tiny synthetic downloaders based on type
    if ds.type == "gtsrb":
        subprocess.run(["python","scripts/download_gtsrb.py"], check=True)
        storage_uri = "s3://securevision/gtsrb"
    elif ds.type in ("ffpp","dfdc"):
        subprocess.run(["python","scripts/download_ffpp.py"], check=True)
        storage_uri = f"s3://securevision/{ds.type}"
    else:
        raise HTTPException(400, "Unsupported dataset type")
    row = Dataset(name=ds.name, version=ds.version, type=ds.type, storage_uri=storage_uri, checksum="")
    db.add(row); db.commit(); db.refresh(row)
    return {"id": row.id, "storage_uri": storage_uri}

@router.get("")
def list_datasets(db: Session = Depends(get_db)):
    return db.query(Dataset).all()
