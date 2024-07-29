#defines the database model for the articles. 
# it's like a blueprint for what info we store about each article, like the title, content, summary, and published date.

from app import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
