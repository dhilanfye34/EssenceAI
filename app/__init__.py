from flask import Flask
from flask.cli import AppGroup

def create_app():
    app = Flask(__name__)

    # Your app initialization code here

    # Create a custom command group
    article_cli = AppGroup('articles')

    # Add the fetch_articles command
    @article_cli.command('fetch')
    def fetch_articles_command():
        from app import fetch_articles  # Import your fetch function
        fetch_articles()

    # Register the command with the Flask CLI
    app.cli.add_command(article_cli)

    return app
