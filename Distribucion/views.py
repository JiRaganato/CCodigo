from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Presupdistform
from .models import Producto,Presupdist
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def ventamayorista(request):

    return render(request, "Distribucion/ventamayorista.html")

def contactodist(request):

    return render(request, "Distribucion/contactodist.html")

def noticias(request):

    return render(request, "Distribucion/noticias.html")

def buscarproddist(request):

    return render(request, "Distribucion/buscarproddist.html")

def buscardist(request):
    nombre = request.GET.get('nombre')
    if nombre:
        resultado = Producto.objects.filter(nombre__icontains=nombre)
        print(nombre)
        print(resultado)
        return render(request, "Distribucion/buscarproddist.html", {"Resultado":resultado})
    
    else:
        resultado = "No se encuentra el producto"
    
    return HttpResponse(resultado)

def productos(request):
    productos = Producto.objects.all()
    return render(request, "Distribucion/buscarproducto.html", {'productos':productos})

class productoslist(ListView):
    model = Producto
    template_name = "Distribucion/productosdist.html"

class productodetalle(DetailView):
    model = Producto
    template_name = "Distribucion/productosdetalle.html"

class productocreacion(CreateView):
    model = Producto
    success_url = "/Distribucion/productosdist/list"
    fields = ['nombre', 'caracteristica']

class productoedit(UpdateView):
    model = Producto
    success_url = "/Distribucion/productosdist/list"
    fields = ['nombre', 'caracteristica']

class productoborrar(DeleteView):
    model = Producto
    success_url = "/Distribucion/productosdist/list"

def presupuestodist(request):
    
    if request.method == 'POST':
        nuevopresupuestodist = Presupdistform(request.POST)
        print(nuevopresupuestodist)
        if nuevopresupuestodist.is_valid():
            informacion = nuevopresupuestodist.cleaned_data
            presupuesto = Presupdist(nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], mail=informacion['mail'], pedido=informacion['pedido'])
            presupuesto.save()
            return render(request, "Distribucion/presupuestodist.html")

    else:
        nuevopresupuestodist = Presupdistform()

    return render(request, "Distribucion/presupuestodist.html", {"nuevopresupuestodist":nuevopresupuestodist})

