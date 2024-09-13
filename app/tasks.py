from app import celery
from email.mime.text import MIMEText
import smtplib

@celery.task
def send_email_async(recipient_email):
    # Example email sending function using SMTP
    msg = MIMEText('This is the email content')
    msg['Subject'] = 'Your Subject'
    msg['From'] = 'youremail@example.com'
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.mailserver.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login('your_email_username', 'your_password')
        server.sendmail('youremail@example.com', recipient_email, msg.as_string())