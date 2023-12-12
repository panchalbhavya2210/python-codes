from django.db import models


# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
