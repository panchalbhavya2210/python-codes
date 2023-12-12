from django.contrib import admin
from .models import Category, BookInfo, Author, Country, State, City


# Register your models here.


class showCateg(admin.ModelAdmin):
    list_display = ('cat_name',)


admin.site.register(Category, showCateg)

class showBookInfo(admin.ModelAdmin):
    list_display = ('book_name', 'book_info', 'book_price', 'book_quantity', 'book_desc', 'book_page', 'bookPhoto', 'cat_name')

admin.site.register(BookInfo, showBookInfo)

class showAuthor(admin.ModelAdmin):
    list_display = ('author_name','auther_gender','author_email','authorImage','author_description')

admin.site.register(Author, showAuthor)

class showCountry(admin.ModelAdmin):
    list_display =('country_name',)

admin.site.register(Country, showCountry)


class showState(admin.ModelAdmin):
    list_display = ('country_name', 'state_name')

admin.site.register(State, showState)


class showCity(admin.ModelAdmin):
    list_display = ('state_name', 'city_name')

admin.site.register(City, showCity)
