from django.shortcuts import render
from .models import registerUser


# Create your views here.

def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        uemail = request.POST.get("email address")
        profileSeeking = request.POST.get("profileSeeking")
        password = request.POST.get('password')
        fName = request.POST.get("username")
        lName = request.POST.get("lastusername")
        gend = request.POST.get("gender")
        religion = request.POST.get("rel")
        mtoo = request.POST.get("mtounge")

        insertData = registerUser(email=uemail, profileSeeking=profileSeeking, firstName=fName, password=password, lastName=lName,
                                  gender_m=gend, rel=religion, mto=mtoo)
        insertData.save()
    return render(request, 'index.html')
