from django.db import models
from django.utils import timezone
# Create your models here.


class Categories(models.Model):

    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):  # Returns name field of model as string.
        return(self.name)


class Catalog(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.PROTECT, related_name='items')
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.name)


class Inventory(models.Model):
    product = models.OneToOneField(Catalog, on_delete=models.PROTECT)
    stock = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.stock)

class Images(models.Model):
    name = models.CharField(max_length=30)

