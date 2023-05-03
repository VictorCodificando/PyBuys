from django.contrib import admin

# Register your models here.

from .models import Productos, Categorias


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'grupo', 'subgrupos')
    ordering = ('grupo__nombre', 'nombre',)
    search_fields = ('nombre', 'grupo__nombre',)
    def subgrupos(self, obj):
        return "\n".join([p.nombre for p in obj.categorias_set.all()])

admin.site.register(Categorias, CategoriasAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'precio', 'rebaja', 'get_precio_real', 'cantidad', 'categoria', 'creado')
    ordering=('nombre', 'precio', 'rebaja', 'cantidad', 'categoria', 'creado')
    search_fields=('nombre', 'precio', 'rebaja', 'cantidad', 'categoria__nombre', 'creado')
    list_filter=('categoria', 'creado')
    date_hierarchy='creado'
    fieldsets=(
        ('Información básica', {
            'fields':('nombre', 'precio', 'rebaja', 'cantidad', 'categoria')
        }),
        ('Imagen', {
            'fields':('image',)
        }),
        ('Descripción', {
            'fields':('descripcion',)
        }),
    )
    readonly_fields=('creado',)
    def get_precio_real(self, obj):
        return obj.get_precio_real()
    get_precio_real.short_description = 'Precio real'
    get_precio_real.admin_order_field = 'precio'
    


admin.site.register(Productos)