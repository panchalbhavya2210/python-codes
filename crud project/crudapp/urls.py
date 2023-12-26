from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index.html"),
    path('insert', views.reg, name='insert'),
    path("peoples", views.fetchData , name="peoples")
]