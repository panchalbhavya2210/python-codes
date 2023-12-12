from django.contrib import admin
from .models import contactus


# Register your models here.

class showcontact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'timestamp']


admin.site.register(contactus, showcontact)
