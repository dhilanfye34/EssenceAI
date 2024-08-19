from app import create_app
from app.scheduler import start_scheduler
from fetch_articles import fetch_articles

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        fetch_articles()  # Manually trigger fetching of articles before starting the app
        start_scheduler()  # Start the scheduler for continuous fetching
    app.run(debug=True)
