from django.shortcuts import render
from .models import contactus

# Create your views here.

def signup(request):
    return render(request, 'signup.html')


def viewdata(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        uphone = request.POST.get('phone')
        umsg = request.POST.get('msg')
        insertquery = contactus(name=uname, email=uemail, phone=uphone, message=umsg)
        insertquery.save()
    return render(request, 'signup.html')