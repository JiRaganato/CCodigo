from django.urls import path
from . import views
urlpatterns = [
    
    path('ventaminorista/', views.ventaminorista, name= "ventaminorista"),
    path('contactocorr/', views.contactocorr, name="contactocorr"),
    path('noticiascorr/', views.noticias, name="noticiascorr"),
    path('productos/', views.productos, name="productos"),
    path('presupuestos/', views.presupuestos, name="presupuestos"),
    path('presupuestosall/', views.presupuestosall, name="presupuestosall"),
    path('borrarpresupuesto/<presupuesto_nombre>/', views.borrarpresupuesto, name="borrarpresupuesto"),
    path('editarpresupuesto/<presupuesto_nombre>/', views.editarpresupuesto, name="editarpresupuesto"),
]