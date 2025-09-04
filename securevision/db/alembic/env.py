from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from securevision.db.models import Base
from securevision.db.session import init_engine
from securevision.config import settings

config = context.config
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(url=settings.DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = init_engine(settings.DATABASE_URL)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
