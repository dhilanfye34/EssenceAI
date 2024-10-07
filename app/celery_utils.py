from celery import Celery

def make_celery(app):
    broker_url = 'redis://:p6b70e6c03e323706f5f42ada9ff93b0e8aeb1d933ae458cd587504e00fb71951@ec2-44-219-154-188.compute-1.amazonaws.com:14219'
    print(f"Celery is using broker: {broker_url}")

    celery = Celery(app.import_name, broker=broker_url)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery