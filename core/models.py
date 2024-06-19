
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class TipoObras(models.Model):
    tecnica = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tecnica


class Producto(models.Model):
    codigo_producto = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    imagen = CloudinaryField('imagen')
    tecnica = models.ForeignKey(TipoObras, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    imagen = CloudinaryField('imagen')
    usuario_producto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cantidad} of {self.nombre_producto}"
    
class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50)
   

    def __str__(self):
        return self.tipo
    

class Usuario(models.Model):
    codigo_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    correo = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=30)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nombre_usuario
   

class OrdenCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total_carrito = models.IntegerField()  
    def __str__(self):
        return f"Compra de {self.usuario.nombre_usuario} el {self.fecha_compra}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='detalles_compra', null=True)  

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} en la compra de {self.compra.fecha_compra}"