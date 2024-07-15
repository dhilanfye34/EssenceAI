#sets up the routes for our web app. 
# it has the logic for handling requests to the main page and fetching articles from the database to display them.

from flask import Blueprint, jsonify, render_template
from app.models import db, Article

main_bp = Blueprint('main', __name__)

@main_bp.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return jsonify([{
        'title': article.title,
        'summary': article.summary,
        'published_date': article.published_date
    } for article in articles])

@main_bp.route('/', methods=['GET'])
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)
