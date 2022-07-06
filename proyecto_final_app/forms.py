from  django import forms


class pokemonformulario(forms.Form):
    
    generacion=forms.CharField(max_length=60)
    numero_generacion=forms.IntegerField()
    