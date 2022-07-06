from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "proyecto_final_app/index.html")




def busqueda_pokemon(request):
    return render(request, "proyecto_final_app/busqueda.html")