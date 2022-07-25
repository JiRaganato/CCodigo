from django.db import models
from django.forms import BooleanField

# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=30)
    caracteristica= models.CharField(max_length=100)

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Producto: {self.nombre} - {self.caracteristica}"

class Presupdist(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    telefono= models.IntegerField()
    mail= models.EmailField()
    pedido= models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Presupuesto: {self.apellido} - {self.created}"


