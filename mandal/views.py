from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from core.forms import MandalForm
from .models import Mandal


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MandalForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('mandal.index')

        else:
            data = Mandal.objects.all().values()
            return render(request, 'mandal/index.html', {'data': data})
    else:
        return redirect("login")

def create(request):
    if request.user.is_authenticated:
        form = MandalForm()
        return render(request, 'mandal/create.html', {'form': form})
    else:
        return redirect("login")

def update(request,id):
    if request.method == 'POST':
        mandal = Mandal.objects.get(id = id)
        form = MandalForm(request.POST,instance = mandal)
        if(form.is_valid()):
            form.save()
            return redirect('mandal.index')

def edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            mandal = Mandal.objects.get(id=id)
            form = MandalForm(instance=mandal)
            return render(request, 'mandal/edit.html', {'data': form,'id':id})
    else:
        return redirect("login")
