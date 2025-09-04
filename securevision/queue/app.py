from celery import Celery
from securevision.config import settings

celery_app = Celery("securevision", broker=settings.REDIS_URL, backend=settings.REDIS_URL)
celery_app.conf.task_default_queue = "default"
