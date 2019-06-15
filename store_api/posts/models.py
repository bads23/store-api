from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    Title = models.CharField(max_length=50)
    Subtitle = models.CharField(max_length=50)
    Content = models.TextField(max_length=1000)
    Cover_Image = models.ImageField(blank=True, upload_to='', default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Events(models.Model):
    Title = models.CharField(max_length=100)
    Venue = models.CharField(max_length=50)
    Date = models.DateField()
    content = models.CharField(max_length=100)
    tickets_link = models.URLField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name