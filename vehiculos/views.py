from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
from vehiculos.forms import *


def vehiculos(request):
    return render(request, "vehiculos/inicio.html")

def autos(request):

    return render(request, "vehiculos/autos.html")

def motos(request):
    return render(request, "vehiculos/motos.html")

def bicicletas(request):
    return render(request, "vehiculos/bicicletas.html")

def autosFormulario(request):
    if request.method=="POST":
        form= AutosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Marca = info["marca"]
            Anio_salida = info["anio_salida"]
            Color = info["color"]
            auto= Autos(marca = Marca, anio_salida = Anio_salida, color = Color)
            auto.save()
            return render (request, "vehiculos/inicio.html", {"mensaje": "auto creado"})
        else:
            return render (request, "vehiculos/inicio.html", {"mensaje": "error"})
    else:
        form = AutosFormulario()
    return render (request, 'vehiculos/autosformulario.html', {"formulario": form})


def motosFormulario(request):
    if request.method=="POST":
        form= MotosFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Marca = info["marca"]
            Anio_salida = info["anio_salida"]
            Color = info["color"]
            auto= Motos(marca = Marca, anio_salida = Anio_salida, color = Color)
            auto.save()
            return render (request, 'vehiculos/inicio.html', {"mensaje": "moto creada"})
        else:
            return render (request, 'vehiculos/inicio.html', {"mensaje": "error"})
    else:
        form= MotosFormulario()
    return render (request, 'vehiculos/motosformulario.html',{"formulario": form})

def biciFormulario(request):
    if request.method=="POST":
        form= BiciFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            Marca = info["marca"]
            Anio_salida = info["anio_salida"]
            Color = info["color"]
            auto= Bicicletas(marca = Marca, anio_salida = Anio_salida, color = Color)
            auto.save()
            return render (request, 'vehiculos/inicio.html', {"mensaje": " bicicleta creada"})
        else:
            return render (request, 'vehiculos/inicio.html', {"mensaje": "error"})
    else:
        form= BiciFormulario()
    return render (request, 'vehiculos/biciformulario.html',{"formulario": form})

def buscarauto(request):
        return render (request, "vehiculos/buscarauto.html" )

def buscarmoto(request):
        return render (request, "vehiculos/buscarmoto.html")

def buscarbici(request):
        return render (request, "vehiculos/buscarbici.html")

def busqueda1(request):
    
    marcasdeauto = request.GET["marca"]
    autos=Autos.objects.filter(marca = marcasdeauto)
    if len(autos)!=0:
        return render(request, "vehiculos/resultadobusqueda.html", {"autos": autos})
    else:
        return render(request, "vehiculos/resultadobusqueda.html", {"mensaje":"no hay autos"})

def busqueda2(request):
 
    marcasdemoto = request.GET["marca"]
    motos=Motos.objects.filter(marca = marcasdemoto)
    if len(motos)!=0:
        return render(request, "vehiculos/resultadobusqueda2.html", {"motos": motos})
    else:
        return render(request, "vehiculos/resultadobusqueda2.html", {"mensaje":"no hay motos"})

def busqueda3(request):
   
    marcasdebici = request.GET["marca"]
    bicicletas=Bicicletas.objects.filter(marca = marcasdebici)
    if len(bicicletas)!=0:
        return render(request, "vehiculos/resultadobusqueda3.html", {"bicicletas": bicicletas})
    else:
         return render(request, "vehiculos/resultadobusqueda3.html", {"mensaje":"no hay bicicletas"})
    


    

