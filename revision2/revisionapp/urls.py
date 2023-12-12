from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('table', views.fetch, name="table.html")
]
