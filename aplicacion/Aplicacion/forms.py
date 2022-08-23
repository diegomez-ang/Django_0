#from socket import fromshare
from django import forms

class CursoForm (forms.Form):
    nombre = forms.CharField( max_length=40)
    camada = forms.IntegerField(max_value=10000)

class BuscaCurso(forms.Form):
    camada = forms.IntegerField()