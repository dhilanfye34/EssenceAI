import os

class Config:
    # Directly use the database URL and ensure the format is correct
    raw_db_uri = os.getenv('DATABASE_URL', 'postgres://u87ggelhtpapvq:p31a412b46a97659c006b2b2522201bc7370c18ff081658f9b67833a287110621@c3gtj1dt5vh48j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dcmogq6mst0e98')
    
    # Replace "postgres://" with "postgresql://" if necessary
    SQLALCHEMY_DATABASE_URI = raw_db_uri.replace("postgres://", "postgresql://", 1) + "?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'BabyLokesh')
    CELERY_BROKER_URL = 'redis://localhost:6380/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6380/0'
    CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
