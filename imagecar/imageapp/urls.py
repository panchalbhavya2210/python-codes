from django.urls import path
from .import views

urlpatterns = [
    path("home", views.index, name='home'),
    path("next", views.nexthtml, name="next"),
    path("nexttwo", views.nexttwo, name="nexttwo")
]
