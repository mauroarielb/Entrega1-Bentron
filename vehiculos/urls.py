from django.urls import path
from .views import *


urlpatterns = [
    path('',vehiculos, name='inicio'),
    path('autos/',autos, name= 'autos'),
    path('motos/',motos, name= 'motos'),
    path('bicicletas/',bicicletas, name= 'bicicletas'),
    path('autosformulario/', autosFormulario, name= 'autosformulario'),
    path('motosformulario/', motosFormulario, name= 'motosformulario'),
    path('biciformulario/', biciFormulario, name= 'biciformulario'),
    path('buscarauto/', buscarauto, name='buscarauto'),
    path('buscarmoto/', buscarmoto, name='buscarmoto'),
    path('buscarbici/', buscarbici, name='buscarbici'),
    path('resultadobusqueda', busqueda1, name='resultadobusqueda'),
    path('resultadobusqueda2', busqueda2, name='resultadobusqueda2'),
    path('resultadobusqueda3', busqueda3 , name='resultadobusqueda3'),

]