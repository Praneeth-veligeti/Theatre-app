from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import *
import random
# Create your views here.

Total_seats = settings.MAX_OCCUPANCY
# Create your views here.
def main(request):
    total = Total_seats
    context = {"total":total}
    return render(request, "theatre/main.html", context)

def occupy(request, pname):
    arr = [i for i in range(1,Total_seats+1)]
    inst = Audience()
    inst.name = pname
    num = Audience.objects.values_list('seatNo')
    print(num)
    for i in num:
        v = i[0]
        arr.remove(i[0])
    print(arr)
    if(len(arr)<1):
        msg="All seats are occupied"
        context={"msg":msg}
        return render(request,"ERROR.html",)
    else:
        seatn = random.choice(arr)
        inst.seatNo = seatn
        inst.save()
        temp = Audience.objects.get(seatNo = seatn)
        context = {"temp":temp}
        return render(request, "theatre/show.html", context)
def get_info(request, pname):
    try:
        inst = Audience.objects.get(name = pname)
        context = {"temp":inst}
    except:
        try:
            inst = Audience.objects.get(ticketId = pname)
            context = {"temp":inst}
        except:
            inst = Audience.objects.get(seatNo = int(pname))
            context = {"temp":inst}

    return render(request, "theatre/show.html", context)


def vacate(request, sn):
    inst = Audience.objects.get(seatNo=sn)
    inst.seatNo = 0
    inst.delete()
    return redirect('main')


