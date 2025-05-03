import smtplib
import csv
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = 'sophiajacob166.com'
PASSWORD = 'Sophia*555*'
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587


def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, to_email, msg.as_string())
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")


with open('contacts.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        to_email = row['email']
        subject = f"Hi {name}, quick update!"
        body = f"Hello {name},\n\nThis is a personalized message just for you.\n\nBest,\nYour Name"

        send_email(to_email, subject, body)

        delay = random.randint(20, 60)
        print(f"⏳ Waiting {delay} seconds before next email...")
        time.sleep(delay)
