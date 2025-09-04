from securevision.db.session import SessionLocal, init_engine
from securevision.config import settings
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db() -> Session:
    init_engine(settings.DATABASE_URL)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
