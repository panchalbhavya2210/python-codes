from django.contrib import admin
from .models import product
# Register your models here.

class addproduct(admin.ModelAdmin):
    list_display = ['productname','productprice','productdesc','product_photo']
admin.site.register(product, addproduct)