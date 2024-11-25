import os
from app import create_app
from app.scheduler import start_scheduler
from asgiref.wsgi import WsgiToAsgi

# Create the Flask app instance
flask_app = create_app()
app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    start_scheduler()
    flask_app.run(host="0.0.0.0", port=port)