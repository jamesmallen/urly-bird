from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField()
