from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.inicio), #esta era nuestra primer view
    path('quienessomos/', views.quienessomos, name="quienessomos"),
    path('contacto/', views.contacto, name="contacto"),
    path('noticias/', views.noticias, name="noticias"),
    path('about/', views.about, name="about"),
    path('construccion/', views.construccion, name="construccion"),
    path('inicio/', views.inicio, name="inicio"),
]