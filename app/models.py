#defines the database model for the articles. 
# it's like a blueprint for what info we store about each article, like the title, content, summary, and published date.

from datetime import datetime
from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)  # Increased length
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=True)
    published_date = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return f'<Article {self.title}>'
