# fetches articles from specified rss feeds, summarizes them using openai, and then stores them in the database. 
# it does the heavy lifting of getting and prepping the article data.

import os
import feedparser
import openai
from datetime import datetime
from app import create_app, db
from app.models import Article

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def fetch_articles():
    feeds = [
        'https://pubmed.ncbi.nlm.nih.gov/rss/search/?term=38906616&limit=10',  # PubMed RSS feed for the specific article
        # Add more RSS feeds if needed
    ]

    for feed in feeds:
        print(f"Fetching from feed: {feed}")  # Debugging line
        parsed_feed = feedparser.parse(feed)
        for entry in parsed_feed.entries:
            try:
                print(f"Fetched article: {entry.title}")  # Debugging line
                # Summarize the article content
                summary = summarize_article(entry.description)
                print(f"Summary: {summary}")  # Debugging line

                # Add article to the database
                article = Article(
                    title=entry.title,
                    content=entry.description,
                    summary=summary,
                    published_date=datetime(*entry.published_parsed[:6])
                )
                db.session.add(article)
            except Exception as e:
                print(f"Error processing article: {e}")  # Debugging line
    db.session.commit()
    print("Articles fetched and stored successfully.")  # Debugging line

def summarize_article(content):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following article: {content}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error summarizing article: {e}")  # Debugging line
        return "Summary not available"

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        fetch_articles()
