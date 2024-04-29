from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombre