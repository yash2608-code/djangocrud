from django.db import models

# Create your models here.
class User(models.Model):
    Fname = models.CharField(max_length=100,null=True)
    Lname = models.CharField(max_length=100,null=True)
    Email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=100)
