from django.urls import path
from AppCC import views
urlpatterns = [
    
    path('', views.inicio), #esta era nuestra primer view
    path('quienessomos', views.quienessomos, name="QuienesSomos"),
    path('contacto', views.contacto, name="Contacto"),
    path('noticias', views.noticias, name="Noticias"),
    path('about', views.about, name="about"),
]