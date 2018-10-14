from django.db import models
from accounts.models import *

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, default="default_name")
    end_datetime = models.DateTimeField()
    users = models.ManyToManyField(User, related_name='users', blank=True)
    pending = models.ManyToManyField(User, related_name='pending', blank=True)
    verified = models.ManyToManyField(User, related_name='verified', blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name