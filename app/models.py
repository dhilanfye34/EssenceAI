from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=True)
    published_date = db.Column(db.DateTime, nullable=False)
    cancer_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'
