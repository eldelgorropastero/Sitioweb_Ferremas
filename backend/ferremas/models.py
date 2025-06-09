import uuid
from django.db import models

class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_producto = models.CharField(max_length=60)
    precio_producto = models.IDecimalField()
    marca_producto = models.CharField(max_length=20)
    stock_producto = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_producto
    

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128) 

    def __str__(self):
        return self.nombre_completo