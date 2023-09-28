from django.contrib import admin
from GestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tfno", "direccion")
    search_fields = ("nombre", "tfno")


cla

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)