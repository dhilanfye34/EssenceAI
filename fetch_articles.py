# fetches articles from specified rss feeds, summarizes them using openai, and then stores them in the database. 
# it does the heavy lifting of getting and prepping the article data.

import os
import feedparser
from openai import OpenAI

client = OpenAI(api_key='sk-proj-rQsYupZksCtjPA1DGXrrT3BlbkFJMzwUpwrDLnJhXrJ7FcQm')
from datetime import datetime
from app import create_app, db
from app.models import Article

# Set your OpenAI API key directly (not recommended for production)

def fetch_articles():
    feeds = [
        'https://pubmed.ncbi.nlm.nih.gov/rss/search/1lQlR_8mqnmeUSTELIMlEQtMXMlcA8QwShAsylr6loJanRIQ76/?limit=15&utm_campaign=pubmed-2&fc=20240715111953',  # Your provided RSS feed link
    ]

    for feed in feeds:
        print(f"Fetching from feed: {feed}")  # Debugging line
        parsed_feed = feedparser.parse(feed)
        if parsed_feed.entries:
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
                    print(f"Adding article to DB: {article}")  # Debugging line
                    db.session.add(article)
                except Exception as e:
                    print(f"Error processing article: {e}")  # Debugging line
        else:
            print("No entries found in the feed.")  # Debugging line
    try:
        db.session.commit()
        print("Articles fetched and stored successfully.")  # Debugging line
    except Exception as e:
        print(f"Error committing to DB: {e}")  # Debugging line

def summarize_article(content):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": (
                    f"Summarize the following article in a detailed and lengthy manner, "
                    f"but ensure it is easily understandable for someone without a medical background. "
                    f"Simplify and explain all key ideas, medical terminology, and concepts to enhance comprehension: {content}"
                )}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error summarizing article: {e}")  # Debugging line
        return "Summary not available"

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        fetch_articles()
