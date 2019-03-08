from django.db import models
from django.utils import timezone
# Create your models here.

class Orders(models.Model):
    name = models.CharField(max_length=50)
    status = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    total = models.IntegerField()