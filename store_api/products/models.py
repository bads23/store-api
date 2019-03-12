from django.db import models
from django.utils import timezone
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    is_active = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)
