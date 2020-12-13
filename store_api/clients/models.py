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
    category = models.ForeignKey(
        Clients_category, on_delete=models.PROTECT, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    soundcloud = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Clients, on_delete=models.PROTECT)
    image = models.CharField(max_length=50, null=True, blank=True)
    audio = models.CharField(max_length=50, null=True, blank=True)
    video = models.CharField(max_length=50, null=True, blank=True)
    plays = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.artist.name)


class About(models.Model):
    '''
        I can't be arsed to create another django app just for this model.
        These fields hold info to be displayed on the about page.
    '''

    about = models.CharField(max_length=2000, null=True, blank=True)
    target = models.CharField(max_length=2000, null=True, blank=True)
    vision = models.CharField(max_length=2000, null=True, blank=True)
    mission = models.CharField(max_length=2000, null=True, blank=True)
    identity = models.CharField(max_length=2000, null=True, blank=True)
