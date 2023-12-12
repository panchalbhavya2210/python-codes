from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home.html")


def nexthtml(request):
    return render(request, "next.html")


def nexttwo(request):
    return render(request, "nexttwo.html")