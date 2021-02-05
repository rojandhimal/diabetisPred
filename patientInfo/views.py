from django.shortcuts import render
from django.http import HttpResponse
from .models import patient
# Create your views here.
def Home(request):
    return render(request,'index.html',{})


def login(request):
    return render(request, 'login.html',{})


def register(request):
    if request.method == "GET":
        username = request.GET.get('username', '') 
        pswd = request.GET.get('password', '') 
        print("username {} password {}".format(username,pswd)) 
        if len(username) and len(pswd) != '':
            p = patient(username=username,password=pswd)
            p.save()
        return render(request, 'register.html',{})
    else:
        return render(request, 'register.html',{})

