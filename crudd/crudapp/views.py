from django.shortcuts import render
from .models import registerD


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        uemail = request.POST.get('email address')
        upassword = request.POST.get('password')
        uselecttype = request.POST.get('profileSeeking')


        insertQuery = registerD(email=uemail, password=upassword, usel=uselecttype)
        insertQuery.save()
    return render(request, 'index.html')
