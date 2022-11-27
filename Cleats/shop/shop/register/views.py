from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


#Checks if the form(sign up) is valid and if so then saves the info, if not then error message is given

def register(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("index")                
    else:
        form= RegisterForm()

    return HttpResponseRedirect(reverse('register'))