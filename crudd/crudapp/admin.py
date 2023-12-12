from django.contrib import admin
from .models import registerD
# Register your models here.


class showRegister(admin.ModelAdmin):
    list_display = ['email', 'password', 'password2', 'profileSeeking', 'firstName', 'lastName', 'gender', 'religion', 'motherT']
admin.site.register(registerD, showRegister)

