
from django.db import models

# Create your models here.
class pokemon(models.Model):
    Tipo=models.CharField(max_length=20)
    Peso=models.FloatField()
    Numero=models.IntegerField()
    Nombre_pokemon=models.CharField(max_length=60)
    Fecha=models.DateField()
    
    
class entrenador(models.Model):
    
    nombre_entrenador=models.CharField(max_length=60)
    numero_entrenador=models.CharField(max_length=60)
    ciudad_entrenador=models.CharField(max_length=60)
    edad=models.IntegerField()
    nacimiento=models.DateField()
    
class gimnasio(models.Model):
    
    nombre_gimnasio=models.CharField(max_length=60)
    ciudad_gimnasio=models.CharField(max_length=60)
    cantidad_habitantes=models.IntegerField()
    
class pokemonEst(models.Model):
    
    Atk=models.IntegerField()
    Def=models.IntegerField()
    Spd=models.IntegerField()
    
class Obj(models.Model):
    
    Efec=models.CharField(max_length=300)
    porcentaje=models.FloatField()
    

    