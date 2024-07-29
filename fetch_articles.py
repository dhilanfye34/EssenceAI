import os
import feedparser
import openai
from datetime import datetime
from app import create_app, db
from app.models import Article

openai.api_key = 'sk-proj-rQsYupZksCtjPA1DGXrrT3BlbkFJMzwUpwrDLnJhXrJ7FcQm'

def fetch_articles():
    feeds = [
        'https://pubmed.ncbi.nlm.nih.gov/rss/search/1lQlR_8mqnmeUSTELIMlEQtMXMlcA8QwShAsylr6loJanRIQ76/?limit=15&utm_campaign=pubmed-2&fc=20240715111953',
    ]

    for feed in feeds:
        print(f"Fetching from feed: {feed}")
        parsed_feed = feedparser.parse(feed)
        if parsed_feed.entries:
            for entry in parsed_feed.entries:
                try:
                    title = entry.title[:200]  # Truncate title to 200 characters
                    print(f"Fetched article: {title}")
                    summary = summarize_article(entry.description)
                    print(f"Summary: {summary}")

                    article = Article(
                        title=title,
                        content=entry.description,
                        summary=summary,
                        published_date=datetime(*entry.published_parsed[:6])
                    )
                    print(f"Adding article to DB: {article}")
                    db.session.add(article)
                except Exception as e:
                    print(f"Error processing article: {e}")
        else:
            print("No entries found in the feed.")
    try:
        db.session.commit()
        print("Articles fetched and stored successfully.")
    except Exception as e:
        print(f"Error committing to DB: {e}")

def summarize_article(content):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": (
                    f"Summarize the following article in a detailed and lengthy manner, "
                    f"but ensure it is easily understandable for someone without a medical background. "
                    f"Simplify and explain all key ideas, medical terminology, and concepts to enhance comprehension: {content}"
                )}
            ],
            max_tokens=250,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return "Summary not available"

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        fetch_articles()
