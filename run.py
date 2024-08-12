from app import create_app, db
from app.models import Article  # Assuming you have an Article model
from flask_migrate import upgrade
import os

app = create_app()

with app.app_context():
    # Apply database migrations to ensure the schema is up to date
    upgrade()

    # Trigger the RSS feed processing function
    # This assumes you have a function `fetch_articles` that processes the feeds and populates the database
    from fetch_articles import fetch_articles
    fetch_articles()  # Run your function to fetch and summarize articles

if __name__ == "__main__":
    app.run()
