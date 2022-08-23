from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import cursos, estudiantes, inicio
from Aplicacion.views import inicio,cursos , profesores, estudiantes, entregables, buscar_curso


urlpatterns = [
    path('',inicio, name = 'AplicacionInicio'), #va al inicio
    path('cursos/', cursos, name = 'Cursos'),
    path('profesores/', profesores,name = 'Profesores'),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('busqueda_curso', buscar_curso)

]