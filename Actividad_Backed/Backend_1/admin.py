from django.contrib import admin
from Backend_1.models import *


# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display-("nombre", "apellido", "numero_cc", "correo", "id_compra")
    search_file-("id_compra",)
    list_filter-("id_compra",)

class ventasAdmin(admin.ModelAdmin):
    list_display-("id_producto", "contidad", "vendedor", "fecha")
    search_file-("id_producto")
    list_filter-("vendedor", "id_producto")

class inventarioAdmin(admin.ModelAdmin):
    list_display-("producto", "cantidad_bodega", "valor_bodega", "fecha_entrega")
    search_fields-("producto")
    list_filter-("producto", "cantidad_bodega")

admin.site.register(clientes, clientesAdmin)
admin.site.register(ventas, ventasAdmin)
admin.site.register(inventario, inventarioAdmin)
