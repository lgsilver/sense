from __future__ import unicode_literals

from django.db import models

class Metrics(models.Model):
    temperature = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
