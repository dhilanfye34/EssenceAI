from app import create_app
from app.scheduler import start_scheduler
from asgiref.wsgi import WsgiToAsgi

# Create the Flask app instance
flask_app = create_app()
app = WsgiToAsgi(flask_app)  # Wrap the Flask app with ASGI compatibility

if __name__ == "__main__":
    start_scheduler()  # Start the scheduler for continuous fetching
    flask_app.run(debug=False)