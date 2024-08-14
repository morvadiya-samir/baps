from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from core.forms import KhsetraForm
from .models import Khsetra


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = KhsetraForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('khsetra.index')

        else:
            data = Khsetra.objects.all().values()
            return render(request, 'khsetra/index.html', {'data': data})
    else:
        return redirect("login")

def create(request):
    if request.user.is_authenticated:
        form = KhsetraForm()
        return render(request, 'khsetra/create.html', {'form': form})
    else:
        return redirect("login")

def update(request,id):
    if request.method == 'POST':
        khsetra = Khsetra.objects.get(id = id)
        form = KhsetraForm(request.POST,instance = khsetra)
        if(form.is_valid()):
            form.save()
            return redirect('khsetra.index')

def edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            khsetra = Khsetra.objects.get(id=id)
            form = KhsetraForm(instance=khsetra)
            return render(request, 'khsetra/edit.html', {'data': form,'id':id})
    else:
        return redirect("login")
