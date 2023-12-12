from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def fetch(request):
    if request.method == "POST":
        name=request.POST.get("uname")
        email=request.POST.get("uemail")
        phone=request.POST.get("uphone")
        address=request.POST.get("address")


        context = {
            "USERNAME":name,
            "USEREMAIL":email,
            "USERPHONE":phone,
            "USERADDRESS":address
        }

    return render(request, 'index.html', context)
