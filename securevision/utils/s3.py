from minio import Minio
from securevision.config import settings

def client():
    return Minio(
        settings.S3_ENDPOINT.replace("http://","").replace("https://",""),
        access_key=settings.S3_ACCESS_KEY,
        secret_key=settings.S3_SECRET_KEY,
        secure=settings.S3_SECURE,
    )
