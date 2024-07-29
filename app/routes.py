#sets up the routes for our web app. 
# it has the logic for handling requests to the main page and fetching articles from the database to display them.

from flask import render_template
from app import app
from app.models import Article

@app.route('/')
def home():
    articles = Article.query.all()
    return render_template('home.html', articles=articles)

