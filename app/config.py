import os

class Config:
    # Database settings (replace 'postgres://' with 'postgresql://')
    raw_db_uri = os.getenv('DATABASE_URL', 'postgres://your-default-db-url')
    SQLALCHEMY_DATABASE_URI = raw_db_uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery configuration - Forcefully use Redis
    CELERY_BROKER_URL = 'redis://:p6b70e6c03e323706f5f42ada9ff93b0e8aeb1d933ae458cd587504e00fb71951@ec2-44-219-154-188.compute-1.amazonaws.com:14219'
    CELERY_RESULT_BACKEND = 'redis://:p6b70e6c03e323706f5f42ada9ff93b0e8aeb1d933ae458cd587504e00fb71951@ec2-44-219-154-188.compute-1.amazonaws.com:14219'
    