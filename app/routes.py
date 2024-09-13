from flask import Blueprint, render_template, request, redirect, url_for, flash
from fetch_articles import feeds  # Import the feeds dictionary
from app.models import Article, Subscriber
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Extract cancer types from the feeds dictionary keys
    return render_template('index.html')

@main.route('/cancer/<cancer_type>')
def cancer(cancer_type):
    # Fetch articles from the database for the selected cancer type
    articles = Article.query.filter_by(cancer_type=cancer_type).all()
    return render_template('cancer.html', cancer_type=cancer_type, articles=articles)

##for navbar
@main.route('/navbar')
def navbar():
    return render_template('nav_bar.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/cancerList')
def cancerList():
    cancer_types = list(feeds.keys())
    return render_template('cancerList.html', cancer_types=cancer_types)

@main.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')  # Get email from form

    # Check if email is already subscribed
    existing_subscriber = Subscriber.query.filter_by(email=email).first()

    if existing_subscriber:
        flash('You are already subscribed!', 'warning')
    else:
        # Add new subscriber to the database
        new_subscriber = Subscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        flash('Thank you for subscribing!', 'success')

    return redirect(url_for('main.index'))  # Redirect back to the homepage
    