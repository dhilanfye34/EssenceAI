from app import celery
from email.mime.text import MIMEText
import smtplib

@celery.task
def send_email_async(recipient_email):
    # Example email sending function using SMTP
    msg = MIMEText('This is the email content')
    msg['Subject'] = 'EssenceAI'
    msg['From'] = 'aiessence86@gmail.com'
    msg['To'] = recipient_email

   
    try:
        with smtplib.SMTP('smtp.mailserver.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login('aiessence86@gmail.com', 'WEssence1!')
            server.sendmail('aiessence86@gmail.com', recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")