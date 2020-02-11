from django.db import models
from datetime import datetime
from django.utils import timezone
from store_api.products.models import Catalog
from store_api.users.models import CustomUser
from store_api.payments.models import Payments, PaymentModes
import string, random
import uuid

from .mailor import send_email

def generateOrderName(user_id):
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    now = datetime.now().strftime("%d%m%y")
    new_name = '{}-{}-{}'.format(user_id, randomstr, now)
    return new_name

class Postas(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Orders(models.Model):
    name = models.CharField(max_length=50, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=0)
    payment = models.ForeignKey(Payments, on_delete=models.PROTECT, null=True, blank=True)
    delivery = models.ForeignKey(Postas, on_delete=models.PROTECT, null=True, blank=True)
    payment_mode =  models.ForeignKey(PaymentModes, on_delete=models.PROTECT, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default=1, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if(self.name == ''):
            self.name = generateOrderName(self.user.id)
        super(Orders, self).save(*args, **kwargs)


class OrderItems(models.Model):

    order = models.ForeignKey(Orders, on_delete=models.CASCADE , related_name='order_items', null=True, blank=True)
    product = models.ForeignKey(Catalog, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    buying_price = models.IntegerField(default=1)
    delivery_fee = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return 'Order item {} from the order {}'.format(self.order, self.product)

