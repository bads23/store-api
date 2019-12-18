from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    Title = models.CharField(max_length=500)
    Subtitle = models.CharField(max_length=500)
    Content = models.TextField(max_length=10000)
    Cover_Image = models.CharField(max_length=500, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

class Events(models.Model):
    Title = models.CharField(max_length=100)
    Venue = models.CharField(max_length=50)
    Date = models.DateField()
    content = models.CharField(max_length=100)
    tickets_link = models.URLField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title

class PostViews(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)


class EventsViews(models.Model):
    post = models.ForeignKey(Events, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)