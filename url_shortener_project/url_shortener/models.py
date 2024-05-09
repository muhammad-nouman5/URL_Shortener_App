from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    long_url = models.URLField(unique=True)
    short_id = models.CharField(max_length=20, unique=True)
    