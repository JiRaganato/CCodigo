from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-Mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Nombre")
    first_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
