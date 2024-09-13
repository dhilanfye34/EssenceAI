from flask import Blueprint, render_template, request, redirect, url_for, flash
from fetch_articles import feeds  # Import the feeds dictionary
from app.models import Article, Subscriber
from . import db
from sqlalchemy.exc import IntegrityError
from app import celery
from email.mime.text import MIMEText
import smtplib
from app.tasks import send_email_async



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
    email = request.form.get('email')

    # Check if the email is already in the database
    existing_subscriber = Subscriber.query.filter_by(email=email).first()

    if existing_subscriber:
        flash('You are already subscribed!', 'warning')
    else:
        try:
            # Add the new subscriber to the database
            new_subscriber = Subscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('Thank you for subscribing!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('There was an error subscribing. Please try again later.', 'danger')

    return redirect(url_for('main.index'))


@main.route('/send_emails')
def send_emails():
    subscribers = Subscriber.query.all()

    # Send emails asynchronously
    for subscriber in subscribers:
        send_email_async.delay(subscriber.email)  # Send email asynchronously using Celery

    flash("Emails are being sent!")
    return redirect(url_for('main.index'))