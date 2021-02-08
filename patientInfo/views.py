from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import patient

from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request,'index.html',{})


def loginPage(request):
    msg = 'msg'
    user = ''
    if request.GET:
        username = request.GET.get('username', '') 
        pswd = request.GET.get('password', '') 
        patients = patient.objects.all()
        print("user from request",request.user)
        
        for p in patients:
            # print(p)
            # print("username {} pswd {}".format(username,pswd))
            # print(" from db username {} pswd {}".format(p.username,p.password))
            if(p.username) == username:
                if(p.password) == pswd:
                   return render(request, 'dashboard.html',context = {'msg':msg,'user':username})
                else:
                    msg = "Incorrect password"
                    print("msg =>",msg)
                    return render(request, 'login.html',context= {'msg':msg,'user':username})
            else:
                msg = "Incorrect username"
                print("msg=>",msg)
                return render(request, 'login.html',{'msg':msg,'user':username})
        
    else:
        return render(request, 'login.html',{msg:'msg',user:'username'})


def registerPage(request):
    form = UserCreationForm()
    if request.GET:
        username = request.GET.get('username', '') 
        pswd = request.GET.get('password', '') 
        print("username {} password {}".format(username,pswd)) 
        if len(username) and len(pswd) != '':
            p = patient(username=username,password=pswd)
            p.save()
        return redirect('login')
    else:
        return render(request, 'register.html',{})


def patientInfo(request):
    return render(request, 'patientinfoform.html',{})


def chart(request):
    username = "ROjan"
    return render(request, 'chart.html',{})

