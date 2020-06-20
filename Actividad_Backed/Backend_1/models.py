from django.db import models


# Create your models here.

class clientes (models.Model):
    numero_cc = models.IntegerField()
    id_compra = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    producto = models.CharField(max_length=20)
    correo = models.EmailField(blank=True, null=True)


class ventas (models.Model):
    vendedor = models.CharField(max_length=30)
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField()


class inventario (models.Model):
    cantidad_bodega = models.IntegerField()
    producto = models.CharField(max_length=20)
    valor_bodega = models.IntegerField()
    fecha_entrega = models.DateField()
