from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def table(request):
    return render(request, 'table.html')


def fetch(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lname = request.POST.get("last name")
        email = request.POST.get("email")
        pnumber = request.POST.get("phone number")
        tot = request.POST.get("type_of_trip")
        cot = request.POST.get("class_of_trip")
        dc = request.POST.get("dep_country")
        destcount = request.POST.get("dest_country")
        text = request.POST.get("text")
        Time = request.POST.get("Time")
        text2 = request.POST.get("Text2")
        Time2 = request.POST.get("Time2")
        aair = request.POST.get("aairport")
        numlug = request.POST.get("numluggage")
        al_name = request.POST.get("al_name")
        fligh_num = request.POST.get('number')
        noa = request.POST.get('noa')
        noc = request.POST.get('noc')
        hotel = request.POST.get('hotel')
        how = request.POST.get('how')
        number2 = request.POST.get('number2')
        text3 = request.POST.get('text3')
        msg = request.POST.get('Message')

        context = {
            "name": name,
            "lname": lname,
            "email": email,
            "pnumber": pnumber,
            "tot": tot,
            "cot": cot,
            "dc": dc,
            "destcount": destcount,
            "text": text,
            "Time": Time,
            "text2": text2,
            "Time2": Time2,
            "aair": aair,
            "numlug": numlug,
            "al_name": al_name,
            "fligh_num": fligh_num,
            "noa": noa,
            "noc": noc,
            "hotel": hotel,
            "how": how,
            "number2": number2,
            "text3": text3,
            "msg": msg,
        }

    return render(request, "table.html", context)


