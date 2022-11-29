from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#Checks if the form(sign up) is valid and if so then saves the info, if not then error message is given

def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")                
    else:
        form= RegisterForm()

    return render(request, "register/register.html", {"form":form}) 


def registration(request):
    
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
             messages.info(request, 'incorrect login details') 


    context={}
    return render(request, "register/login.html", context) 

def logoutUser(request):
    logout(request)
    return redirect('login')