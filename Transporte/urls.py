from django.urls import path
from . import views
urlpatterns = [
    
    path('transporte/', views.transporte, name="transporte"),
    path('contactotransp/', views.contactotransp, name="contactotransp"),
    path('noticiastransp/', views.noticias, name="noticiastransp"),
]