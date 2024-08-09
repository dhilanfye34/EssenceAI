from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from app import create_app, fetch_articles
import threading

app = create_app()

def start_fetching_articles():
    with app.app_context():
        fetch_articles()

if __name__ == '__main__':
    # Initialize the scheduler
    scheduler = BackgroundScheduler()
    # Add the job to fetch articles every hour
    scheduler.add_job(fetch_articles, 'interval', hours=1)
    scheduler.start()

    # Start fetching articles in a background thread
    fetch_thread = threading.Thread(target=start_fetching_articles)
    fetch_thread.start()

    # Start the Flask server
    app.run(debug=True)

    # Wait for the fetch thread to finish before shutting down
    fetch_thread.join()

    try:
        # Start the Flask server
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
