from django.db import models
from django.utils import timezone

# Create your models here.


class Clients_category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    profile_photo = models.ImageField(blank=True, upload_to='', default='')
    category = models.ForeignKey(Clients_category ,on_delete=models.PROTECT)
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    soundcloud = models.URLField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name