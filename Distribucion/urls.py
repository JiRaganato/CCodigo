from django.urls import path
from . import views
urlpatterns = [
    
    path('ventamayorista/', views.ventamayorista, name= "ventamayorista"),
    path('contactodist/', views.contactodist, name="contactodist"),
    path('noticiasdist/', views.noticias, name="noticiasdist"),
    path('buscarproddist/', views.buscarproddist, name="buscarproddist"),
    path('presupuestodist', views.presupuestodist, name="presupuestodist"),
    path('buscar', views.buscardist, name= "buscardist"),
]