import africastalking


username = "sandbox"
api_key = "bc61395826d01968700a375de623ff59728781f42d9b429103284bb112b06300"

africastalking.initialize(username, api_key)

payments = africastalking.Payment

product_name = 'MTA_MPESA'
phone_number = '+254728753983'

currency_code = 'KES'
amount = 100.50

def pay():

  try:
    response = payments.mobile_checkout(product_name, phone_number, currency_code, amount)
    print(response)
  except Exception as e:
    print(e)

pay()