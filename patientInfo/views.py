from django.shortcuts import render
from django.http import HttpResponse
from .models import patient
# Create your views here.
def Home(request):
    return render(request,'index.html',{})


def login(request):
    if request.method == "GET":
        username = request.GET.get('username', '') 
        pswd = request.GET.get('password', '') 
        patients = patient.objects.all()
        user = ''
        for p in patients:
            print(p)
            print("username {} pswd {}".format(username,pswd))
            print(" from db username {} pswd {}".format(p.username,p.password))
            if(p.username) == username:
                if(p.password) == pswd:
                   return render(request, 'dashboard.html',{user:user})
                else:
                    return render(request, 'login.html',{})
            else:
                return render(request, 'login.html',{})
        
    else:
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


def patientInfo(request):
    return render(request, 'patientinfoform.html',{})

