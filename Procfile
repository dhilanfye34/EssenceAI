web: uvicorn app:app --host 0.0.0.0 --port ${PORT}
worker: celery -A app.celery worker --loglevel=info