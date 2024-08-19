from flask import Blueprint, render_template
from fetch_articles import feeds  # Import the feeds dictionary
from .models import Article

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Extract cancer types from the feeds dictionary keys
    cancer_types = list(feeds.keys())
    return render_template('index.html', cancer_types=cancer_types)

@main.route('/cancer/<cancer_type>')
def cancer(cancer_type):
    # Fetch articles from the database for the selected cancer type
    articles = Article.query.filter_by(cancer_type=cancer_type).all()
    return render_template('cancer.html', cancer_type=cancer_type, articles=articles)
