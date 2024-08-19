from flask import render_template
from app import db
from app.models import Article
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cancer/<cancer_type>')
def cancer_articles(cancer_type):
    articles = Article.query.filter_by(cancer_type=cancer_type).distinct(Article.title).all()
    return render_template('articles.html', articles=articles)
