#!/usr/bin/env python

import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.conf import settings
from decouple import Config, RepositoryEnv


BASE_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", ".."))      
ENV_FILE = os.path.join(BASE_DIR, '.env')
config = Config(RepositoryEnv(ENV_FILE))


def send_email(email):
    smtp_server = config('SMTP_SERVER')
    port = config('SMTP_PORT')
    sender_email = config('SENDER_EMAIL')
    password = config('EMAIL_PASS')
    receiver_email = email
    text = "Hello Steve! You can now send email notifications using python!"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    part1 = MIMEText(text, "plain")
    message.attach(part1)


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string() )

