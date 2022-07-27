from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('usarname')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "AppCC/login.html", {"mensaje":f"Bienvenido{usuario}"})
            
            else:
                return render(request, "AppCC/login.html", {"Error datos incorrectos"})
        
        else:
            return render(request, "AppCC/login.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "AppCC/login.html", {'form':form})
