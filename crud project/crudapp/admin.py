from django.contrib import admin
from .models import registerUser


# Register your models here.

class adminShow(admin.ModelAdmin):
    list_display = ['email', 'profileSeeking', 'firstName', 'lastName', 'gender_m', 'rel', 'mto']


admin.site.register(registerUser, adminShow)
