from django.urls import path
from Corralon import views
urlpatterns = [
    
    path('ventaminorista', views.ventaminorista, name= "VentaMinorista"),
    path('contacto', views.contacto, name="Contacto"),
    path('noticias', views.noticias, name="Noticias"),
    path('buscarproducto', views.buscarproducto),
]