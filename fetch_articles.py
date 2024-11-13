import os
import feedparser
import openai
from app import db
from datetime import datetime
from app.models import Article

# Set your OpenAI API key
openai.api_key = 'sk-proj-rQsYupZksCtjPA1DGXrrT3BlbkFJMzwUpwrDLnJhXrJ7FcQm'

# Cancer types and their corresponding RSS feeds
feeds = {
    'Breast Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1lIZdG7__acNiPnxLwe9dievbtT2ykZDpzmhH1M37avlc_J9bK/?limit=15&utm_campaign=pubmed-2&fc=20240809224835',
    'Lung Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1LU7YBGfC-yGn9EL0yPGew-Gfn5lHWl42C5hi-GsswhqdckAAq/?limit=15&utm_campaign=pubmed-2&fc=20240806135434',
    'Prostate Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1TQbL92JdzY1vfZj3Ovsk-ka-tW8-AczOWGhdGMm0nLqb9Lkb5/?limit=15&utm_campaign=pubmed-2&fc=20240806135459',
    'Colorectal Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1fqLZM0XwJj9UKgNserBqe5YfFZSGWgcHJpsp5MCwqvqdIGM9d/?limit=15&utm_campaign=pubmed-2&fc=20240806135529',
    'Melanoma (Skin Cancer)': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1671MaA5CeAK2phosesnsfeFMRpDxz0CCEMtJCQDz6QNQKJoDX/?limit=15&utm_campaign=pubmed-2&fc=20240806135610',
    'Bladder Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1deGMjvjVspl9jz0d-xRss-fBpBLefxC-Hdtt8i61uO8_HM9gZ/?limit=15&utm_campaign=pubmed-2&fc=20240806135627',
    'Kidney Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/18_r98JPP6yYzruDW4q8njym7ick7pLc0PK1VXFZY1wwBJ15N4/?limit=15&utm_campaign=pubmed-2&fc=20240806135642',
    'Liver Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1d1GIw6PmDzsQvBiiIYgGJSoG4VonM1p6dZ9QYEo_Qhy44KQEP/?limit=15&utm_campaign=pubmed-2&fc=20240806135704',
    'Pancreatic Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1PeFS8XE8OyGjjpfTB_OxFMJoBciLDOMQ30MBdHINSM9WQV9VQ/?limit=15&utm_campaign=pubmed-2&fc=20240806135726',
    'Thyroid Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1loZZVJsOLJdgLdcVC30XLjg-1uI3IHqFDtuGTvdP8ugZQTkHW/?limit=15&utm_campaign=pubmed-2&fc=20240806135817',
    'Leukemia': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1z_pxc-9fhPXGP3MZzTXHOj9kXHvYhp58BNAWHOLBUkLZUpkFm/?limit=15&utm_campaign=pubmed-2&fc=20240806135837',
    'Lymphoma (Hodgkin and Non-Hodgkin)': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1tsh1RBFJ1LZwnp5i06tCJQkzA58j1rLIWkwKgnGhNimqJQEDX/?limit=15&utm_campaign=pubmed-2&fc=20240806135855',
    'Ovarian Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1-_PV-NYr61fGx-L-nxjiaCNZkMcG4pNURY_qf9_gv_vRiJgsr/?limit=15&utm_campaign=pubmed-2&fc=20240806135911',
    'Endometrial Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1bipEQobMwpVqZxUYelrvblAcqGgMdT9bLE4V5EqfdhzYmbYd-/?limit=15&utm_campaign=pubmed-2&fc=20240806135932',
    'Cervical Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1-cNR3TsrjMBfqp6d-PNzCh-guTILM3PGqNs79XYuKolm4G98X/?limit=15&utm_campaign=pubmed-2&fc=20240806135956',
    'Esophageal Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1rwwlo3vxyKzzgfdtuid1sWTLSxEV4VX0tOpC5jz7CNSF56UXL/?limit=15&utm_campaign=pubmed-2&fc=20240806140310',
    'Stomach Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1tKhRtdb-g-umDKXOF2O9xrFsyTWWZZWFfwJX1Olr83bOfash5/?limit=15&utm_campaign=pubmed-2&fc=20240806140337',
    'Brain and Spinal Cord Tumors': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1RAka_j-eJMm9n-uxXnnHLxJlMdsSh23kW9I0_GqGZ7yEYGUUi/?limit=15&utm_campaign=pubmed-2&fc=20240806140400',
    'Testicular Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1h3SAs98aPqrd6V8zl4HtQGH-cKg8ZcyMVrYXN6rzzSuCSUk38/?limit=15&utm_campaign=pubmed-2&fc=20240806140516',
    'Bone Cancer': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1tObSykPNCPx0bSIOf-nIncu-DY64NYfYeuquOYGgeaSCafgM6/?limit=15&utm_campaign=pubmed-2&fc=20240806140529',
    'Soft Tissue Sarcoma': 'https://pubmed.ncbi.nlm.nih.gov/rss/search/1NKSH3UhXTzQteDpfyzgD1YQdSQt8dOi1qvuYWUuPO0I39LQND/?limit=15&utm_campaign=pubmed-2&fc=20240806140544',
}

def fetch_articles():
    for cancer_type, feed in feeds.items():
        print(f"Fetching from feed: {feed}")
        parsed_feed = feedparser.parse(feed)
        if parsed_feed.entries:
            # Fetch only the first article for testing
            entry = parsed_feed.entries[0]
            try:
                # Check if the article already exists in the database
                existing_article = Article.query.filter_by(title=entry.title, published_date=datetime(*entry.published_parsed[:6])).first()
                
                if existing_article is None:
                    print(f"Fetched article: {entry.title}")
                    summary = summarize_article(entry.description)
                    print(f"Summary: {summary}")

                    # Add article to the database
                    article = Article(
                        title=entry.title,
                        content=entry.description,
                        summary=summary,
                        published_date=datetime(*entry.published_parsed[:6]),
                        cancer_type=cancer_type
                    )
                    db.session.add(article)
                else:
                    print(f"Article already exists in the database: {entry.title}")

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
                    f"Simplify and explain all key ideas, medical terminology, and concepts to enhance comprehension. "
                    f"Make it really long and detailed though and explain every single terminology that we enounter: {content}"
                )}
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return "Summary not available"
