from pyexpat import model
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=123)
    bithday = models.DateField()