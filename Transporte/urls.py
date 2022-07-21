from django.urls import path
from . import views
urlpatterns = [
    
    path('transporte/', views.transporte, name="transporte"),
    path('contactotransp/', views.contacto, name="contactotransp"),
    path('noticiastransp/', views.noticias, name="noticiastransp"),
]