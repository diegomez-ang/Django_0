from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Template
from Aplicacion.models import Curso
# Create your views here.

def curso(request, nombre, camada):
    cur = Curso(nombre = nombre, camada = camada)
    cur.save()
    plantilla = loader.get_template('curso.html')#carga plantilla
    contexto = {# crea un contexto
        'nombre': cur.nombre ,
        'camada': cur.camada
    }
    documento = plantilla.render(contexto) #renderiza

    return HttpResponse(documento) #retorna el documento