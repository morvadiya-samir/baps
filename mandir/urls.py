from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='mandir.index'),      
    path("create/", views.create, name='mandir.create'),      
    path("update/<id>/", views.update, name='mandir.update'),      
    path("edit/<id>/", views.edit, name='mandir.edit')    
    
]
