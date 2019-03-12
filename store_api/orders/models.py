from django.db import models
from django.utils import timezone
from store_api.products.models import Catalog
from store_api.users.models import CustomUser
from store_api.payments.models import Payments
# Create your models here.

class Orders(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=0)
    total = models.IntegerField(default=0)
    payment = models.ForeignKey(Payments, on_delete=models.PROTECT, null=True, blank=True)
    status = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str(self):
        return 'Order item {} from the order {}'.format(self.order, self.product)