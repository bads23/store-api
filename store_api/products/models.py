from django.db import models
from django.utils import timezone
from rest_framework.serializers import ValidationError


class Categories(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):  # Returns name field of model as string.
        return(self.name)


class Subcategories(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='category')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.name)


class Productclass(models.Model):
    name = models.CharField(max_length=30)
    subcategory = models.ForeignKey(
        Subcategories, on_delete=models.CASCADE, related_name='productclass')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.name)


class Catalog(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='items')
    subcategory = models.ForeignKey(
        Subcategories, on_delete=models.CASCADE, related_name='subcategory', null=True, blank=True
    )
    productclass = models.ForeignKey(
        Productclass, on_delete=models.CASCADE, related_name='productclass', null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.name)


class Inventory(models.Model):
    product = models.OneToOneField(
        Catalog, on_delete=models.CASCADE, related_name='stock')
    stock = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(self.stock)


class Images(models.Model):
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name='images')
    path = models.FileField(upload_to="images/", null=True, blank=True)
    is_avatar = models.BooleanField(null=True)

    def __str__(self):
        return(self.path)

    def validate_is_avatar(self):
        # Check is there is an entry with is_avatar set as true
        images = self.__class__.objects.filter(is_avatar=True)

        if images.count() > 0:
            for res in images:
                res.is_avatar = False
                res.save()

    def save(self, *args, **kwargs):
        if self.is_avatar == True:
            self.validate_is_avatar()
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
