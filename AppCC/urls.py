from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('', views.inicio), #esta era nuestra primer view
    path('quienessomos/', views.quienessomos, name="quienessomos"),
    path('noticias/', views.noticias, name="noticias"),
    path('about/', views.about, name="about"),
    path('construccion/', views.construccion, name="construccion"),
    path('inicio/', views.inicio, name="inicio"),
    path('contacto/', views.contacto, name="contacto"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCC/logout.html'), name = 'Logout'),
    path('editarperfil', views.editarperfil, name="editarperfil"),
]