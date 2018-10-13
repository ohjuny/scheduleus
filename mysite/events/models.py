from django.db import models
from accounts.models import *

# Create your models here.
class FreeTime(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    
class Event(models.Model):
    users = models.ManyToManyField(User)
    end_datetime = models.DateTimeField()
    free_times = models.ManyToManyField(FreeTime)
    count = models.IntegerField()
