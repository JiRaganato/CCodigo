from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ventaminorista(request):

    return render(request, "Corralon/ventaminorista.html")

def contacto(request):

    return render(request, "Corralon/contacto.html")

def noticias(request):

    return render(request, "Corralon/noticias.html")

def buscarproducto(request):

    return render(request, "Corralon/productos.html")

def productos(request):

    return render(request, "Corralon/productos.html")