import os

class Config:
    raw_db_uri = os.getenv('DATABASE_URL', 'postgres://your-default-db-url')
    SQLALCHEMY_DATABASE_URI = raw_db_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery configuration - Make sure it uses Redis
    CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    