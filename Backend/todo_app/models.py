from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False,blank=False)

object = models.Manager()

def __str__(self):
    return self.title

