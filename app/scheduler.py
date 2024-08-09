from apscheduler.schedulers.background import BackgroundScheduler
from fetch_articles import fetch_articles

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_articles, 'interval', hours=1)
    scheduler.start()
