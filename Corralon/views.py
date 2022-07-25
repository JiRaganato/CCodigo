from http.client import NOT_FOUND
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import Presupcorrform
from .models import Productos, Presupcor
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

def contactocorr(request):

    return render(request, "Corralon/contactocorr.html")

def noticias(request):

    return render(request, "Corralon/noticias.html")

def buscarproducto(request):

    return render(request, "Corralon/productos.html")

def productos(request):
    productos = Productos.objects.all()
    return render(request, "Corralon/productos.html", {'productos':productos})