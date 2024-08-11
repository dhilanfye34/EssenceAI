from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from app import create_app, fetch_articles, db  # Ensure `db` is imported

app = create_app()

if __name__ == '__main__':
    # Initialize the scheduler
    scheduler = BackgroundScheduler()
    # Add the job to fetch articles every hour
    scheduler.add_job(fetch_articles, 'interval', hours=1)
    scheduler.start()

    # Fetch articles initially
    with app.app_context():
        db.create_all()  # This will create tables if they don't exist
        fetch_articles()

    try:
        # Start the Flask server
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
