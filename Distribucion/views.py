from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

from CCodigo.Corralon.models import Productos
from CCodigo.Distribucion.models import Producto, producto

# Create your views here.

def ventamayorista(request):

    return render(request, "Distribucion/ventamayorista.html")

def contacto(request):

    return render(request, "Distribucion/contacto.html")

def noticias(request):

    return render(request, "Distribucion/noticias.html")

def buscarproducto(request):

    return render(request, "Distribucion/buscarproducto.html")

def productos(request):
    productos = Producto.objects.all()
    return render(request, "Distribucion/buscarproducto.html", {'productos':productos})
