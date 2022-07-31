from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppCC.forms import UserEditForm
from .models import Avatar

# Create your views here.

def inicio(request):

    if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user = request.user.id)

        return render(request, "AppCC/inicio.html", {"url":avatares[0].imagen.url})
    else:
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
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                return render(request, "AppCC/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                
            else:
                return render(request, "AppCC/login.html", {"mensaje":"Error contraseña incorrecta"})
        
        else:
            return render(request, "AppCC/login.html", {"mensaje":"Error, el usuario no existe"})
    
    form = AuthenticationForm()

    return render(request, "AppCC/login.html", {'form':form})

def register(request):
    if request. method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCC/login.html", {"mensaje":"Usuario creado"})
    
    else:
        form = UserCreationForm()
    
    return render(request, "AppCC/register.html", {"form":form})

@login_required
def editarperfil(request):
    usuario= request.user

    if request.method == "POST":
        miformulario = UserEditForm(request.POST)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppCC/inicio.html")
    
    else:
        miformulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppCC/editarperfil.html", {"miformulario":miformulario, "usuario":usuario})

