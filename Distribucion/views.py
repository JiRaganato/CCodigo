from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ventamayorista(request):

    return render(request, "Distribucion/ventamayorista.html")

def contacto(request):

    return render(request, "Distribucion/contacto.html")

def noticias(request):

    return render(request, "Distribucion/noticias.html")

def buscarproducto(request):

    return render(request, "Distribucion/buscarproducto.html")
