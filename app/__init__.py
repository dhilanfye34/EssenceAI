# sets up the flask app and configures the database. 
# it initializes the app and database, creates the necessary tables, and registers the main routes blueprint.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

from app import routes, models
