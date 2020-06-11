# https://stackoverflow.com/questions/2809547/creating-email-templates-with-django

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string      
from .models import Orders, OrderItems

def send_order_email(req):
    order = Orders.objects.get(id=req['order'])
    order_items = OrderItems.objects.filter(order=req['order']) 

    delivery_fee = 0
    for res in order_items:
        delivery_fee += res.delivery_fee 

    subject = "Order Received!"
    text = "Your Order has been recieved!"
    html = render_to_string('order_email_admin.html', {"order":order, "order_items":order_items, "delFee": delivery_fee})
    sender = 'motiontafrica@gmail.com'
    to = ['stevekaruma@gmail.com']

    try:
        msg = EmailMultiAlternatives(subject, text, sender, to)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        
    except Exception as e:
        print(e)
        return False
   