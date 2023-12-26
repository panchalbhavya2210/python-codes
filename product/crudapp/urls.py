from django.urls import path
from .import views

urlpatterns = [
    path('', views.showproductpage, name="showproduct"),
    path('addproduct', views.addproductpage, name="addproduct"),
    path('insertproductdata', views.insertproductdata, name="insertproductdata")
]