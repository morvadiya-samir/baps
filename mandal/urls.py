from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='mandal.index'),      
    path("create/", views.create, name='mandal.create'), 
    path("update/<id>/", views.update, name='mandal.update'),      
    path("edit/<id>/", views.edit, name='mandal.edit')    
    
]
