from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Polls(models.Model):
    end_date = models.CharField(max_length=50)
    title = models.CharField(max_length=3000)
    excerpt = models.CharField(max_length=3000)
    client = models.CharField(max_length=3000)
    location = models.CharField(max_length=3000)
    url = models.CharField(max_length=3000)
