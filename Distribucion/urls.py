from django.urls import path
from . import views
urlpatterns = [
    
    path('ventamayorista/', views.ventamayorista, name= "ventamayorista"),
    path('contactodist/', views.contactodist, name="contactodist"),
    path('noticiasdist/', views.noticias, name="noticiasdist"),
    path('buscarproddist/', views.buscarproddist, name="buscarproddist"),
    path('presupuestodist', views.presupuestodist, name="presupuestodist"),
    path('buscar', views.buscardist, name= "buscardist"),
    path('curso/list', views.productoslist.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.productodetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.productocreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.productoedit.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.productoborrar.as_view(), name='Delete'),
]