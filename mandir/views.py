from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from core.forms import MandirForm
from .models import Mandir
from django.core import serializers


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MandirForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('mandir.index')

        else:
            # data = serializers.serialize('json', Mandir.objects.all())
            data = Mandir.objects.all().values()
            return render(request, 'mandir/index.html', {'data': data})
    else:
        return redirect("login")

def update(request,id):
    if request.method == 'POST':
        mandir = Mandir.objects.get(id = id)
        form = MandirForm(request.POST,instance = mandir)
        if(form.is_valid()):
            form.save()
            return redirect('mandir.index')

def create(request):
    if request.user.is_authenticated:
        form = MandirForm()
        return render(request, 'mandir/create.html', {'form': form})
    else:
        return redirect("login")

def edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            mandir = Mandir.objects.get(id=id)
            form = MandirForm(instance=mandir)
            return render(request, 'mandir/edit.html', {'data': form ,'id':id})
    else:
        return redirect("login")
