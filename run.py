from app import create_app
from app.scheduler import start_scheduler

app = create_app()

if __name__ == "__main__":
    start_scheduler()  # Start the scheduler for continuous fetching
    app.run(debug=False)
