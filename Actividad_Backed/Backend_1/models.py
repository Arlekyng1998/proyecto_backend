from django.db import models
from secrets import token_hex

# Create your models here.

#Random token >=32 bytes para que sea seguro
def radom():
    token_hex(64)

class clientes(model.Model):
    numero_cc-models.IntegerField()
    id_compra-models.IntegerField(radom())
    nombre-models.CharField(max_length-30)
    apellido-models.CharField(max_length-20)
    producto-models.CharField(max_length-20)
    correo-models.EmailField(blank=True, null=True)

class ventas(model.Model):
    vendedor-models.CharField(max_length-30)
    id_producto-models.IntegerField()
    contidad-models.IntegerField()
    fecha-models.DateField()

class inventario(model.Model):
    cantidad_bodega-models.IntegerField()
    producto-models.CharField(max_length-20)
    valor_bodega-models.IntegerField()
    fecha_entrega-models.DateField()
