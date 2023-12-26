from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class product(models.Model):
    productname = models.CharField(max_length=50)
    productprice = models.FloatField()
    productdesc = models.TextField()
    productimage = models.ImageField(upload_to='photos')

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"'.format(self.productimage.url))