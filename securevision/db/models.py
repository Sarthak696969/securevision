from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, JSON, ForeignKey, DateTime, Text
import datetime as dt

Base = declarative_base()

class Dataset(Base):
    __tablename__ = "datasets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    version: Mapped[str] = mapped_column(String(32))
    type: Mapped[str] = mapped_column(String(32))
    storage_uri: Mapped[str] = mapped_column(Text, default="")
    checksum: Mapped[str] = mapped_column(String(128), default="")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

class ModelDef(Base):
    __tablename__ = "modeldefs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    arch: Mapped[str] = mapped_column(String(32))
    task: Mapped[str] = mapped_column(String(32))
    params_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

class Experiment(Base):
    __tablename__ = "experiments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), default="")
    task: Mapped[str] = mapped_column(String(32), default="")
    dataset_id: Mapped[int] = mapped_column(ForeignKey("datasets.id"))
    modeldef_id: Mapped[int] = mapped_column(ForeignKey("modeldefs.id"))
    config_yaml: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(32), default="pending")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)
    started_at: Mapped[dt.datetime | None]
    finished_at: Mapped[dt.datetime | None]

class Artifact(Base):
    __tablename__ = "artifacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    experiment_id: Mapped[int] = mapped_column(ForeignKey("experiments.id"))
    kind: Mapped[str] = mapped_column(String(32))
    path: Mapped[str] = mapped_column(Text)
    size_bytes: Mapped[int] = mapped_column(Integer, default=0)
    checksum: Mapped[str] = mapped_column(String(128), default="")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

class Metric(Base):
    __tablename__ = "metrics"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    experiment_id: Mapped[int] = mapped_column(ForeignKey("experiments.id"))
    key: Mapped[str] = mapped_column(String(64))
    value_float: Mapped[float] = mapped_column(Float)
    context_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    celery_id: Mapped[str] = mapped_column(String(64))
    type: Mapped[str] = mapped_column(String(32))
    status: Mapped[str] = mapped_column(String(32), default="pending")
    request_json: Mapped[str] = mapped_column(Text, default="{}")
    result_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)

class FederatedRun(Base):
    __tablename__ = "federated_runs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    base_experiment_id: Mapped[int] = mapped_column(Integer)
    num_clients: Mapped[int] = mapped_column(Integer)
    malicious_frac: Mapped[float] = mapped_column(Float)
    aggregator: Mapped[str] = mapped_column(String(32))
    status: Mapped[str] = mapped_column(String(32), default="pending")
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)
