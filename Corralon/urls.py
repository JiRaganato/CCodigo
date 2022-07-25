from django.urls import path
from . import views
urlpatterns = [
    
    path('ventaminorista/', views.ventaminorista, name= "ventaminorista"),
    path('contactocorr/', views.contactocorr, name="contactocorr"),
    path('noticiascorr/', views.noticias, name="noticiascorr"),
    path('productos/', views.productos, name="productos"),
    path('presupuestos/', views.presupuestos, name="presupuestos"),
]