import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    project = models.CharField(max_length=100)
    Description = models.TextField(max_length=500)

