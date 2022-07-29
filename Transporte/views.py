from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Transporte.models import Cargas, Tramos

# Create your views here.

def transporte(request):

    return render(request, "Transporte/transporte.html")

def contactotransp(request):

    return render(request, "Transporte/contactotransp.html")

def noticias(request):

    return render(request, "Transporte/noticias.html")

@login_required
def tramos(request):
    tramos = Tramos.objects.all()
    return render(request, "EN DONDE?", {'Tramo':tramos})

@login_required
def cargas(request):
    cargas = Cargas.objects.all()
    return render(request, "EN DONDE?", {'Carga':cargas})


