import os

class Config:
    # Use the DATABASE_URL from Heroku, or fall back to a local SQLite database for local development
    SQLALCHEMY_DATABASE_URI = os.getenv('postgres://u87ggelhtpapvq:p31a412b46a97659c006b2b2522201bc7370c18ff081658f9b67833a287110621@c3gtj1dt5vh48j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dcmogq6mst0e98', 'sqlite:///local.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
