from django.contrib import admin

# Register your models here.

from .models import Productos, Categorias, Caracteristicas

admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(Caracteristicas)

