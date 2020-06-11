# https://stackoverflow.com/questions/2809547/creating-email-templates-with-django

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_contact_form(req):
    subject = req["subject"]
    message = req["message"]
    name = req["name"]
    email = req["email"]

    html = render_to_string('contact_form.html', {"subject": subject, "name": name, "email": email, "message": message})
    to = ['stevekaruma@gmail.com']
    sender = 'motiontafrica@gmail.com'

    try:
        msg = EmailMultiAlternatives(subject, message, sender, to)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        return True
    except Exception as e:
        print(e)
        return False