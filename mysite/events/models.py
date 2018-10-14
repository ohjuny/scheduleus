from django.db import models
from accounts.models import *

# Create your models here.
class FreeTime(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

class Event(models.Model):
    name = models.CharField(max_length=50, default="default_name")
    end_datetime = models.DateTimeField()
    users = models.ManyToManyField(User, blank=True)
    free_times = models.ManyToManyField(FreeTime)

    def __str__(self):
        return self.name