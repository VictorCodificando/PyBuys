from django.contrib import admin

# Register your models here.

from .models import ProductosEnCarrito, Compras, Ventas

class ComprasAdmin(admin.ModelAdmin):
    list_display=('id_usuario', 'id_producto', 'cantidad', 'creado')
    ordering=('id_usuario', 'id_producto', 'cantidad', 'creado')
    search_fields=('id_usuario', 'id_producto', 'cantidad', 'creado')
    list_filter=('id_usuario', 'id_producto', 'cantidad', 'creado')
    date_hierarchy='creado'
    fieldsets=(
        ('Información básica', {
            'fields':('id_usuario', 'id_producto', 'cantidad')
        }),
        ('Fecha', {
            'fields':('creado',)
        }),
    )
    readonly_fields=('creado','id_usuario')

    def save_model(self, request, obj, form, change):
        obj.id_usuario = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Compras, ComprasAdmin)

class ProductosEnCarritoAdmin(admin.ModelAdmin):
    list_display=('id_usuario', 'producto', 'cantidad')
    ordering=('id_usuario', 'producto', 'cantidad')
    search_fields=('id_usuario', 'producto', 'cantidad')
    list_filter=('id_usuario', 'producto', 'cantidad')
    fieldsets=(
        ('Información básica', {
            'fields':('id_usuario', 'producto', 'cantidad')
        }),
    )

admin.site.register(ProductosEnCarrito, ProductosEnCarritoAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display=('id_usuario', 'id_producto', 'cantidad', 'creado')
    ordering=('id_usuario', 'id_producto', 'cantidad', 'creado')
    search_fields=('id_usuario', 'id_producto', 'cantidad', 'creado')
    list_filter=('id_usuario', 'id_producto', 'cantidad', 'creado')
    date_hierarchy='creado'
    fieldsets=(
        ('Información básica', {
            'fields':('id_usuario', 'id_producto', 'cantidad')
        }),
        ('Fecha', {
            'fields':('creado',)
        }),
    )
    readonly_fields=('creado',)

admin.site.register(Ventas, VentasAdmin)