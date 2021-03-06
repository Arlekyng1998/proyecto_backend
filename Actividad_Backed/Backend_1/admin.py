from django.contrib import admin
from Backend_1.models import *




# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_cc", "correo", "id_compra")
    search_file = ("id_compra", "numero_cc", "id_compra")
    list_filter = ("id_compra",)

class ventasAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "cantidad", "vendedor")
    search_file = ("id_producto", "vendedor")
    list_filter = ("id_producto",)
    date_hierarchy = "fecha"

class inventarioAdmin(admin.ModelAdmin):
    list_display = ("producto", "cantidad_bodega", "valor_bodega")
    search_fields = ("producto", "cantidad_bodega")
    list_filter = ("producto", "cantidad_bodega")
    date_hierarchy = "fecha_entrega"

admin.site.register (clientes, clientesAdmin)
admin.site.register (ventas, ventasAdmin)
admin.site.register (inventario, inventarioAdmin)
