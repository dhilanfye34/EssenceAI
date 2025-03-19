import os

class Config:
    # Corrected PostgreSQL connection string
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://healthcare_user:pens@localhost:5432/healthcare_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery Configuration (If Used)
    CELERY_BROKER_URL = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672//')
    CELERY_RESULT_BACKEND = 'redis://:p6b70e6c03e323706f5f42ada9ff93b0e8aeb1d933ae458cd587504e00fb71951@ec2-44-219-154-188.compute-1.amazonaws.com:14219'
