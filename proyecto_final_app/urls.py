
from django import views
from django.contrib import admin
from django.urls import path,URLPattern
from proyecto_final_app import views

urlpatterns = [
    path("/", views.index),
    path("busqueda/", views.busqueda_pokemon),
]
