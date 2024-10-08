from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .celery_utils import make_celery

db = SQLAlchemy()
celery = None

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    global celery
    celery = make_celery(app)

    from .routes import main
    app.register_blueprint(main)

    return app
