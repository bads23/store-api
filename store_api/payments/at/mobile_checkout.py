#!/usr/bin/env python
import os
import africastalking
from django.conf import settings
from decouple import config, RepositoryEnv
import string
import random
from datetime import datetime


BASE_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))      
# ENV_FILE = os.path.join(BASE_DIR, '.env')
# config = Config(RepositoryEnv(ENV_FILE))

# https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths


def generateOrderName():
    randomstr = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=6))
    now = datetime.now().strftime("%d%m%y")
    new_name = '{}-{}'.format(randomstr, now)
    return new_name


def pay(data):
    username = config('AT_USERNAME')
    api_key = config('AT_API_KEY')
    africastalking.initialize(username, api_key)
    payments = africastalking.Payment
    product_name = config('AT_PRODUCT_NAME')
    phone_number = data['phone_number']
    currency_code = data['currency_code']
    amount = data['amount']
    metadata = {}
    metadata['kyc'] = data['kyc']

    try:
        response = payments.mobile_checkout(
            product_name, phone_number, currency_code, amount, metadata)
        return response
    except Exception as e:
        return e
