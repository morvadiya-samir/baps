from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from core.forms import RegisterForm,LoginForm

def signin(request):
    if request.method == 'POST':
        print("request",request._body)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('dashbord')
    else:
        return render(request, 'authentication/login.html',{"form": LoginForm})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print("rich",form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def dashbord(request):
    if request.user.is_authenticated:
        return render(request, 'dashbord/index.html')
    else:
        return redirect("login")

def account(request):
    if request.user.is_authenticated:
        print("user1",request.user)
        print("user",User.objects.get(id=request.user.id))
        return render(request, 'pages/account.html', {'user': request.user})
    else:
        return redirect("login")

def mandir(request):
    if request.user.is_authenticated:
        print("user",User.objects.get(id=request.user.id))
        return render(request, 'dashbord/mandir/index.html', {'user': request.user})
    else:
        return redirect("login")


