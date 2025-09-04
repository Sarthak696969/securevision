from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from securevision.config import settings

_engine = None
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False))

def init_engine(url: str | None = None):
    global _engine, SessionLocal
    url = url or settings.DATABASE_URL
    _engine = create_engine(url, pool_pre_ping=True)
    SessionLocal.configure(bind=_engine)
    return _engine
