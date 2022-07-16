from django.urls import path
from Transporte import views
urlpatterns = [
    
    path('transporte', views.transporte, name="Transporte"),
    path('contacto', views.contacto, name="Contacto"),
    path('noticias', views.noticias, name="Noticias"),
]