from flask import Flask
from .config import Config  # Updated import statement
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        db.create_all()

    return app
