from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from fetch_articles import fetch_articles  # Import the fetch_articles function
        fetch_articles()  # Automatically fetch articles after the app starts

    from app.routes import main  # Import the Blueprint
    app.register_blueprint(main)

    return app
