from django.db import models
from django.forms import BooleanField

# Create your models here.

class Tramos(models.Model):
    origen= models.CharField(max_length=30)
    destino= models.CharField(max_length=40)
    km= models.IntegerField()
    retorno=BooleanField()

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Tramo: {self.origen} - {self.destino}"

class Cargas(models.Model):
    material= models.CharField(max_length=30)
    empaquetado= models.CharField(max_length=20)
    peso= models.IntegerField()

# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Carga: {self.material} - {self.empaquetado}"
