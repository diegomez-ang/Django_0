from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import cursos, estudiantes, inicio
from Aplicacion.views import inicio,cursos , profesores, estudiantes, entregables


urlpatterns = [
    path('',inicio, name = 'AplicacionInicio'), #va al inicio
    path('cursos/', cursos, name = 'AplicacionCursos'),
    path('profesores/', profesores,),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),

]