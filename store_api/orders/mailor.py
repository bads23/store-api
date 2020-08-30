# https://stackoverflow.com/questions/2809547/creating-email-templates-with-django

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string      
from django.dispatch import receiver
from django.urls import reverse
from .models import Orders, OrderItems
from store_api.users.models import CustomUser
import time


from django_rest_passwordreset.signals import reset_password_token_created

def send_order_email(req):
    time.sleep(60)
    order = Orders.objects.get(id=req['order'])
    order_items = OrderItems.objects.filter(order=req['order'])

    delivery_fee = 0
    total = 0

    for res in order_items:
        delivery_fee += res.delivery_fee
        total += res.delivery_fee + res.product.price


    subject = "Order Received!"
    text = "New Order has been recieved!"
    html = render_to_string('order_email_admin.html', {"order":order, "order_items":order_items, "delFee": delivery_fee, "total": total})
    sender = 'motiontafrica@gmail.com'
    to = ['stevekaruma@gmail.com']

    try:
        msg = EmailMultiAlternatives(subject, text, sender, to)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        
    except Exception as e:
        print(e)
        return False


def send_confirm_email(req):
    time.sleep(10)
    order = Orders.objects.get(id=req['order'])
    order_items = OrderItems.objects.filter(order=req['order'])
    user = CustomUser.objects.get(id=req['user'])

    delivery_fee = 0
    total = 0

    for res in order_items:
        delivery_fee += res.delivery_fee
        total += res.delivery_fee + res.product.price


    subject = "Order Received!"
    text = "Your Order has been recieved!"
    html = render_to_string('order_email_users.html', {"order":order, "order_items":order_items, "delFee": delivery_fee, "total": total, "user":user})
    sender = 'motiontafrica@gmail.com'
    to = ['stevekaruma@gmail.com']

    try:
        msg = EmailMultiAlternatives(subject, text, sender, to)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        
    except Exception as e:
        print(e)
        return False

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'first_name': reset_password_token.user.first_name,
        'email': reset_password_token.user.email,
        'reset_password_url': "https://store.motiontalentafrica.co.ke/?token={}".format(reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('reset_pass_email.html', context)
    email_plaintext_message = 'Use this link to reset password. http://localhost:4000/resetpassword/{} \n If you did not request a password reset, ignore this email. \n \n Warmest Regards, \n The Motion Talent Africa Team.'.format(reset_password_token.key)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Motion Talent Africa Store"),
        # message:
        email_plaintext_message,
        # from:
        'motiontafrica@gmail.com',
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()