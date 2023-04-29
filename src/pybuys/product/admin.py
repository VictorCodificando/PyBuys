from django.contrib import admin

# Register your models here.

from .models import Productos, Categorias

admin.site.register(Productos)
admin.site.register(Categorias)

