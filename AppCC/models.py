from django.db import models
from django.forms import BooleanField

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




