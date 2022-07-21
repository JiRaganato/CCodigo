from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

from CCodigo.Transporte.models import Cargas, Tramos

# Create your views here.

def transporte(request):

    return render(request, "Transporte/transporte.html")

def contacto(request):

    return render(request, "Transporte/contacto.html")

def noticias(request):

    return render(request, "Transporte/noticias.html")

def tramos(request):
    tramos = Tramos.objects.all()
    return render(request, "EN DONDE?", {'Tramo':tramos})

def cargas(request):
    cargas = Cargas.objects.all()
    return render(request, "EN DONDE?", {'Carga':cargas})


