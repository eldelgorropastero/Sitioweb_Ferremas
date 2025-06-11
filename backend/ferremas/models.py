from django.db import models

# Create your models here.
import uuid


class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_producto = models.CharField(max_length=60)
    precio_producto = models.IntegerField()
    marca_producto = models.CharField(max_length=20)
    stock_producto = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_producto
    
