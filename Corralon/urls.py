from django.urls import path
from . import views
urlpatterns = [
    
    path('ventaminorista/', views.ventaminorista, name= "ventaminorista"),
    path('contactocorr/', views.contacto, name="contacto"),
    path('noticiascorr/', views.noticias, name="noticias"),
    path('productos/', views.productos, name="productos"),
]