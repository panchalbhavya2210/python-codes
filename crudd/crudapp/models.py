from django.db import models

# Create your models here.

class registerD(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    profileSeeking = models.TextField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=30)
    motherT = models.CharField(max_length=50)