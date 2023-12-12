from django.urls import path
from .import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('about', views.aboutus, name='about'),
    path('contact', views.contact, name='contact'),
    path('inquiry', views.inquiry, name='inquiry')
]
