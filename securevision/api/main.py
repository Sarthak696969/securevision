from fastapi import FastAPI, Depends, Request
from securevision.api.auth import api_key_auth
from securevision.config import settings
from securevision.logging import setup_logging, request_id_var
from securevision.db.session import init_engine
from securevision.db import models as models_db
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from securevision.api.routers import health, datasets, models, jobs, attacks, defenses, evaluation, xai, federated, artifacts

setup_logging(settings.LOG_LEVEL)
app = FastAPI(title="SecureVision API", version="0.1.0")

# Routers
app.include_router(health.router, prefix="/", tags=["general"])
app.include_router(datasets.router, prefix="/datasets", tags=["datasets"], dependencies=[Depends(api_key_auth)])
app.include_router(models.router, prefix="/models", tags=["models"], dependencies=[Depends(api_key_auth)])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"], dependencies=[Depends(api_key_auth)])
app.include_router(attacks.router, prefix="/experiments", tags=["attacks"], dependencies=[Depends(api_key_auth)])
app.include_router(defenses.router, prefix="/experiments", tags=["defenses"], dependencies=[Depends(api_key_auth)])
app.include_router(evaluation.router, prefix="/experiments", tags=["evaluation"], dependencies=[Depends(api_key_auth)])
app.include_router(xai.router, prefix="/experiments", tags=["xai"], dependencies=[Depends(api_key_auth)])
app.include_router(federated.router, prefix="/federated", tags=["federated"], dependencies=[Depends(api_key_auth)])
app.include_router(artifacts.router, prefix="/experiments", tags=["artifacts"], dependencies=[Depends(api_key_auth)])

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id_var.set(request.headers.get("x-request-id","-"))
    response = await call_next(request)
    return response
