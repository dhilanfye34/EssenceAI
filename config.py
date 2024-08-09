import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://healthcare_user:pens@localhost/healthcare_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
