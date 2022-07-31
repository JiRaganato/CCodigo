from django.db import models
from django.forms import BooleanField
from django.contrib.auth.models import User

# Create your models here.

class presupuesto(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono=models.IntegerField()
    mail = models.EmailField()
    pedido= models.CharField(max_length=200)
    retira= BooleanField()

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcarpeta Avatares de Media
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)





