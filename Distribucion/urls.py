from django.urls import path
from . import views
urlpatterns = [
    
    path('ventamayorista/', views.ventamayorista, name= "ventamayorista"),
    path('contactodist/', views.contacto, name="contactodist"),
    path('noticiasdist/', views.noticias, name="noticiasdist"),
    path('buscarproducto/', views.buscarproducto, name="buscarproducto"),
]