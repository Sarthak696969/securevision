import pytest, os
from securevision.db.session import init_engine, SessionLocal
from securevision.db.models import Base
from sqlalchemy.orm import Session

@pytest.fixture(scope="session", autouse=True)
def db():
    engine = init_engine("sqlite:///./test.db")
    Base.metadata.create_all(engine)
    yield
