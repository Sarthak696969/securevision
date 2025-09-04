# SecureVision

Production-grade backend for **Robust and Explainable Computer Vision Under Adversarial Attacks**.

## Quickstart (Docker)

```bash
docker-compose up --build
```

First run will apply Alembic migrations and start API at `http://localhost:8000/docs`.
A Celery worker, Redis, Postgres, and MinIO are also started.

## Local (Poetry)

```bash
poetry install
poetry run uvicorn securevision.api.main:app --reload
poetry run celery -A securevision.queue.app:celery_app worker -l INFO
```

### Example cURL

Register GTSRB (downloads via script):
```bash
curl -X POST http://localhost:8000/datasets/register -H "x-api-key: dev" -H "content-type: application/json" -d '{
  "name":"gtsrb","type":"gtsrb","version":"1.0"
}'
```

Define model:
```bash
curl -X POST http://localhost:8000/models/define -H "x-api-key: dev" -H "content-type: application/json" -d '{
  "name":"resnet18_gtsrb","arch":"resnet18","task":"gtsrb"
}'
```

Launch training (tiny smoke config):
```bash
curl -X POST http://localhost:8000/experiments/train -H "x-api-key: dev" -H "content-type: application/json" -d '{
  "dataset_id":1,"modeldef_id":1,"training_config":{"epochs":1,"batch_size":16,"lr":0.001,"adv_training":"none","seed":42}
}'
```

Get job status:
```bash
curl http://localhost:8000/jobs/1 -H "x-api-key: dev"
```

> See more examples in `configs/` and routers' OpenAPI examples.

### Environment

Copy `.env.example` to `.env` and adjust as needed.

### Ethics

This repository is for research & defensive purposes. Do not deploy to harm or deceive.
# securevision
