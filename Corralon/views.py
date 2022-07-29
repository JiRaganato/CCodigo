from http.client import NOT_FOUND
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import Presupcorrform
from .models import Productos, Presupcor
from django.contrib.auth.decorators import login_required

# Create your views here.

def ventaminorista(request):

    return render(request, "Corralon/ventaminorista.html")

def presupuestos(request):
    
    if request.method == 'POST':
        nuevopresupuesto = Presupcorrform(request.POST)
        print(nuevopresupuesto)
        if nuevopresupuesto.is_valid():
            informacion = nuevopresupuesto.cleaned_data
            presupuesto = Presupcor(nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], mail=informacion['mail'], pedido=informacion['pedido'], retiro=informacion['retiro'])
            presupuesto.save()
            return render(request, "Corralon/presupuestos.html")

    else:
        nuevopresupuesto = Presupcorrform()

    return render(request, "Corralon/presupuestos.html", {"nuevopresupuesto":nuevopresupuesto})

@login_required
def presupuestosall(request):
    presup = Presupcor.objects.all()
    return render(request, "Corralon/presupuestosall.html", {'presup':presup})

@login_required
def borrarpresupuesto(request, presupuesto_nombre):

    aeliminar = Presupcor.objects.get(nombre=presupuesto_nombre)
    aeliminar.delete()

    presup = Presupcor.objects.all()
    return render(request, "Corralon/presupuestosall.html", {'presup':presup})

@login_required
def editarpresupuesto(request, presupuesto_nombre):

    aeditar = Presupcor.objects.get(nombre=presupuesto_nombre)
    
    if request.method == 'POST':
        mipresupuesto = Presupcorrform(request.POST)
        print(mipresupuesto)
        if mipresupuesto.is_valid():
            nuevainfo = mipresupuesto.cleaned_data

            aeditar.nombre = nuevainfo['nombre']
            aeditar.apellido = nuevainfo['apellido']
            aeditar.telefono = nuevainfo['telefono']
            aeditar.mail = nuevainfo['mail']
            aeditar.pedido = nuevainfo['pedido']
            aeditar.retiro = nuevainfo['retiro']

            aeditar.save()

            return render(request, "Corralon/editarpresupuesto.html")
            

    else:
                
        mipresupuesto = Presupcorrform(initial={'nombre': aeditar.nombre, 'apellido': aeditar.apellido, 'telefono': aeditar.telefono, 'mail':aeditar.mail, 'pedido': aeditar.pedido,'retiro': aeditar.retiro})
    
    return render(request, "Corralon/editarpresupuesto.html", {"mipresupuesto":mipresupuesto, "presupuesto_nombre":presupuesto_nombre})


def contactocorr(request):

    return render(request, "Corralon/contactocorr.html")

def noticias(request):

    return render(request, "Corralon/noticias.html")

@login_required
def buscarproducto(request):

    return render(request, "Corralon/productos.html")

def productos(request):
    productos = Productos.objects.all()
    return render(request, "Corralon/productos.html", {'productos':productos})

@login_required
def borrarproducto(request, producto_nombre):

    producto = Productos.objects.get(producto_nombre)
    producto.delete()

    productos = Productos.objects.all()
    return render(request, "Corralon/productos.html", {'productos':productos})

