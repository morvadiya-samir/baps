from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def dashbord(request):
    if request.user.is_authenticated:
        return render(request, 'dashbord/index.html')
    else:
        return redirect("login")

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    return render(request, 'authentication/register.html')
