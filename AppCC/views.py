from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "AppCC/inicio.html")

def quienessomos(request):

    return render(request, "AppCC/quienessomos.html")


def noticias(request):

    return render(request, "AppCC/noticias.html")

def about(request):

    return render(request, "AppCC/about.html")

def construccion(request):

    return render(request, "AppCC/construccion.html")

def contacto(request):

    return render(request, "AppCC/contacto.html")
