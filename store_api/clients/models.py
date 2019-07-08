from django.db import models
from django.utils import timezone

# Create your models here.


class Clients_category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=1000)
    profile_photo = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Clients_category ,on_delete=models.PROTECT)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    soundcloud = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name