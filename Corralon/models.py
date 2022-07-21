from django.db import models
from django.forms import BooleanField

# Create your models here.

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    caracteristica= models.CharField(max_length=100)
    stock= BooleanField()

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Producto: {self.nombre} - {self.caracteristica}"


