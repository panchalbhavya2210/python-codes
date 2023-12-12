from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('render', views.render, name='render'),
    path('purchase', views.purchase, name='purchase'),
]