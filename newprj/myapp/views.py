from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def inquiry(request):
    return render(request, "inquiry.html")
