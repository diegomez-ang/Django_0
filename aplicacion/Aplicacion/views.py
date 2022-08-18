from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, Template
from Aplicacion.models import Curso
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def cursos(request):
    contexto = {
        'cursos':{
            'curso1': 'Nombre1',
            'curso2': 'Nombre2',
            'curso3': 'Nombre3'
        }
    }
    return render(request, 'cursos.html', contexto)

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return redirect('AplicacionInicio')

def entregables(request):
    return HttpResponse('vista entregables') 