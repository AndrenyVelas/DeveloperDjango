from django.contrib import admin
from .models import cliente, categoria,proveedor, tipoprenda,sastreria,establecimiento,nuevoListado,prendas,compra,producto,venta
# Register your models here.

admin.site.register(cliente)
admin.site.register(categoria)
admin.site.register(proveedor)
admin.site.register(tipoprenda)
admin.site.register(sastreria)
admin.site.register(establecimiento)
admin.site.register(nuevoListado)
admin.site.register(prendas)
admin.site.register(compra)
admin.site.register(producto)
admin.site.register(venta)