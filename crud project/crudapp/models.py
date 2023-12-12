from django.db import models

GENDER = (("male", "Male"), ('female', "Female"))

# Create your models here.

class registerUser(models.Model):
    email = models.EmailField()
    profileSeeking = models.TextField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    gender_m = models.CharField(max_length=20, choices=GENDER)
    rel = models.CharField(max_length=20)
    mto = models.CharField(max_length=20)
