from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from app.routes import main  # Import the Blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load the configuration from the Config class

    db.init_app(app)

    with app.app_context():
        db.create_all()  # This ensures tables are created (for local development)

    # Register the Blueprint
    app.register_blueprint(main)

    return app
