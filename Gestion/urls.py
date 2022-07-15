from django.urls import path
from Gestion import views
urlpatterns = [
    
    path('gestion', views.gestion, name="Gestion"),
]