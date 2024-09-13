from celery import Celery
from email.mime.text import MIMEText
import smtplib

def make_celery(app):
    # Initialize Celery with the app's name and broker URL from config
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():  # Ensuring tasks have the correct app context
                return self.run(*args, **kwargs)

    # Set the task base to the ContextTask
    celery.Task = ContextTask
    return celery