from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("dashbord/", views.dashbord, name='dashbord'),      
    path("login/", views.signin, name='login'),      
    path("register/", views.register, name='register'),      
    path("account/", views.account, name='account'),     
    
]
