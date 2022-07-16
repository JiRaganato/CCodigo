from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def transporte(request):

    return render(request, "Transporte/transporte.html")

def contacto(request):

    return render(request, "Transporte/contacto.html")

def noticias(request):

    return render(request, "Transporte/noticias.html")

