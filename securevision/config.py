from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    ENV: str = Field("dev", description="Environment name")
    API_KEY: str = "dev"
    DATABASE_URL: str = "sqlite:///./sv.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    S3_ENDPOINT: str = "http://localhost:9000"
    S3_ACCESS_KEY: str = "svminio"
    S3_SECRET_KEY: str = "svminiopass"
    S3_BUCKET: str = "securevision"
    S3_SECURE: bool = False
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
