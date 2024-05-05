
from django.db import models

# Create your models here.

class TipoObras(models.Model):
    tecnica = models.CharField(max_length=50)

    def __str__(self):
        return self.tecnica


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    imagen = models.ImageField(null=True, blank=True)
    tecnica = models.ForeignKey(TipoObras, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombre