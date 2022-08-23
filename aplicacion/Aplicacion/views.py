from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, Template
from Aplicacion.models import Curso
from Aplicacion.forms import BuscaCurso, CursoForm

# Create your views here.

def inicio(request):
    return render(request,'Appcoder/index.html')

def cursos(request):
    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada = data.get('camada'))
            curso_data.save()
        else:
            redirect('AplicacionInicio')


    cursos = Curso.objects.all() #carga todo para visualizar
    contexto = {
        'cursos': cursos,
        'my_form': CursoForm()
    }

    return render(request, 'Appcoder/cursos.html', contexto)

def buscar_curso(request):

    curso_buscar = [] #lista
    if request.method == 'POST':
        camada = request.POST.get('camada')
        curso_buscar = Curso.objects.filter(camada__icontains=camada) #trae uno especifico y es con mayuscula por que es un modelo
        

    contexto = {
        'my_form': BuscaCurso,
        'cursos': curso_buscar
    }
    return render(request, 'Appcoder/buscar_curso.html', contexto)

def profesores(request):
    return render(request, 'Appcoder/profesores.html')

def estudiantes(request):
    return redirect('AplicacionInicio')

def entregables(request):
    return HttpResponse('vista entregables') 