from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.celery_utils import make_celery

db = SQLAlchemy()
celery = None  # Placeholder for the Celery instance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    

    with app.app_context():
        db.create_all()

        from fetch_articles import fetch_articles  # Import the fetch_articles function
        fetch_articles()  # Automatically fetch articles after the app starts

    # Initialize Celery after app creation
    global celery
    celery = make_celery(app)

    from app.routes import main  # Import the Blueprint
    app.register_blueprint(main)

    return app
