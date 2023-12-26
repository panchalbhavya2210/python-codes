from django.shortcuts import render
from .models import product
# Create your views here.

def showproductpage(request):
    data=product.objects.all()
    print(data)
    return render(request, 'showproduct.html' , {"productdata": data})


def addproductpage(request):
    return render(request, 'addproduct.html')


def insertproductdata(request):
    prodname = request.POST.get('pname')
    prodprice = request.POST.get('pprice')
    prodesc = request.POST.get('pdesc')
    prodimage = request.FILES['pimage']
    insertquery = product(productname=prodname, productprice=prodprice, productdesc=prodesc, productimage=prodimage)
    insertquery.save()

    return render(request, 'showproduct.html')
