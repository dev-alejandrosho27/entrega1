from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

from proyecto_final_app.models import pokemon

# Create your views here.
def index(request):
    return render(request, "proyecto_final_app/index.html")




def busqueda_pokemon(request):
    
    return render(request, "proyecto_final_app/busqueda.html")



def buscar_pokemon(request):
    
    if request.GET["pokemon"]:
        
        mensaje="articulo buscado: %r" %request.GET["pokemon"]
        pokemon_buscado=request.GET["pokemon"]
        pokemon_Base_Datos=pokemon.objects.filter(nombre__icontains=pokemon_buscado)
        return render(request, "proyecto_final_app/resultado_busqueda.html", {"pokemon buscado":pokemon_buscado,"pokemon en la base de datos":pokemon_Base_Datos})
    else:
        
        mensaje="por favor introduce un pokemon a buscar"
        
    return HttpResponse(mensaje)