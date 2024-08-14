from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='khsetra.index'),      
    path("create/", views.create, name='khsetra.create'), 
    path("update/<id>/", views.update, name='khsetra.update'),      
    path("edit/<id>/", views.edit, name='khsetra.edit')    
    
]
