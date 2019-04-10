#!/usr/bin/env python
import os
import africastalking
from django.conf import settings
from decouple import Config, RepositoryEnv

BASE_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
ENV_FILE = os.path.join(BASE_DIR, '.env')
config = Config(RepositoryEnv(ENV_FILE))

# https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths


def pay(data):
    username = config.get('AT_USERNAME')
    api_key = config.get('AT_API_KEY')
    africastalking.initialize(username, api_key)
    payments = africastalking.Payment
    product_name = config.get('AT_PRODUCT_NAME')
    phone_number = data['phone_number']
    currency_code = data['currency_code']
    amount = data['amount']

    try:
        response = payments.mobile_checkout(
            product_name, phone_number, currency_code, amount)
        return response
    except Exception as e:
        return e
