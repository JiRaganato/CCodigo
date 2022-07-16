from django.urls import path
from Distribucion import views
urlpatterns = [
    
    path('ventamayorista', views.ventamayorista, name= "VentaMayorista"),
    path('contacto', views.contacto, name="Contacto"),
    path('noticias', views.noticias, name="Noticias"),
    path('buscarproducto', views.buscarproducto),
]