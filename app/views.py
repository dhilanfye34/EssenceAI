from flask import render_template
from app.models import Article
import app

@app.route('/cancer_type/<type>')
def show_articles(type):
    articles = Article.query.filter_by(cancer_type=type).all()
    return render_template('cancer.html', articles=articles, cancer_type=type)
