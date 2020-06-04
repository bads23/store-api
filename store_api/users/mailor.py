#!/usr/bin/env python

import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.conf import settings
from django.core.mail import send_mail
from decouple import Config, RepositoryEnv


BASE_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", ".."))      
ENV_FILE = os.path.join(BASE_DIR, '.env')
config = Config(RepositoryEnv(ENV_FILE))


def send_email(email):
    send_mail(
        'Subject here',
        'Here is the message.',
        'motiontafrica@gmail.com',
        ['stevekaruma@gmail.com'],
        fail_silently=False,
    )

