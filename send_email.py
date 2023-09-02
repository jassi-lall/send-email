from os import getenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Check credentials are stored as environment variables
if getenv('gmail_username') == None:
    error_message = """
    Save Gmail username and password as environment variables gmail_username and gmail_password respectively
    Environment variables were not found. Check environment variables and restart any IDE."""
    print(error_message)
    exit(1)

# Set up email parameters
sender_email = getenv('gmail_username')
receiver_email = "INSERT RECIPIENT EMAIL HERE (IN LINE 16 OF PYTHON SCRIPT)"
subject = "Automated message"
message = """
    Hi

    This message has been sent programatically.

    Best wishes

    Bot
    """

# Create email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = sender_email
smtp_password = getenv('gmail_password')

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully")
