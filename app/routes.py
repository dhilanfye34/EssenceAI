from flask import Blueprint, render_template
from .models import Article

# Define the blueprint
main = Blueprint('main', __name__)

# Route for the homepage
@main.route('/')
def index():
    return render_template('index.html')

# Route for displaying cancer-related articles
@main.route('/cancer/<cancer_type>')
def cancer(cancer_type):
    # Query the database for articles of the specified cancer type
    articles = Article.query.filter_by(cancer_type=cancer_type).all()
    return render_template('cancer.html', articles=articles, cancer_type=cancer_type)
