from fastapi import APIRouter
from securevision.config import settings
from securevision.db.session import init_engine
from securevision.db.models import Base
from sqlalchemy import inspect

router = APIRouter()

@router.get("/health")
def health():
    engine = init_engine(settings.DATABASE_URL)
    insp = inspect(engine)
    has_tables = bool(insp.get_table_names())
    return {"status":"ok","env":settings.ENV,"migrations_applied":has_tables}
