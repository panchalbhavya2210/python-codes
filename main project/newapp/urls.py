from django.urls import path
from .import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('insert', views.viewdata, name='insert')
]