from django.db import models
from django.utils.safestring import mark_safe


GENDER = (("1", "Male"), ("2", "Female"))

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name


class BookInfo(models.Model):
    book_name = models.CharField(max_length=40)
    book_info = models.TextField()
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
    book_desc = models.TextField()
    book_page = models.IntegerField()
    book_image = models.ImageField()
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def bookPhoto(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.book_image.url))


class Author(models.Model):
    author_name = models.CharField(max_length=20)
    auther_gender = models.CharField(max_length=20 , choices=GENDER)
    author_email = models.EmailField()
    auther_pp = models.ImageField()
    author_description = models.TextField()


    def authorImage(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.auther_pp.url))


class Country(models.Model):
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return State.state_name

class City(models.Model):
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)