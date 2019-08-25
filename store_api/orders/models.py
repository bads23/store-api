from django.db import models
from datetime import datetime
from django.utils import timezone
from store_api.products.models import Catalog
from store_api.users.models import CustomUser
from store_api.payments.models import Payments
import string, random

import uuid

def generateOrderName(user_id):
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    now = datetime.now().strftime("%d%m%y")
    new_name = '{}-{}-{}'.format(user_id, randomstr, now)
    return new_name

class Orders(models.Model):
    name = models.CharField(max_length=50, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=0)
    total = models.IntegerField(default=0)
    payment = models.ForeignKey(Payments, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(max_length=10, default="PENDING", null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if(self.name == ''):
            self.name = generateOrderName(self.user.id)
        super(Orders, self).save(*args, **kwargs)


class OrderItems(models.Model):

    order = models.ForeignKey(Orders, on_delete=models.CASCADE , related_name='order_items')
    product = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str(self):
        return 'Order item {} from the order {}'.format(self.order, self.product)

class Postas(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)

    def __str(self):
        return self.name