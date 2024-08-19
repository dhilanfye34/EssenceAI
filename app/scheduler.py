from apscheduler.schedulers.background import BackgroundScheduler
from fetch_articles import fetch_articles

def start_scheduler():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(fetch_articles, 'interval', minutes=10)
    scheduler.start()
