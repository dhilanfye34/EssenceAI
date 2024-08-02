from flask import render_template
from app import app
from app.models import Article

@app.route('/')
def home():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)
