from django.db import models
from django.utils import timezone


class Clients_category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=5000)
    tag = models.CharField(max_length=50, null=True, blank=True)
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