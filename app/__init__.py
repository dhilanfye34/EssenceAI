from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration setup
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create tables for our models

    # Register Blueprints and other setup
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
