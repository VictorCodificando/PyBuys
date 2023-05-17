from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

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


class UserAdmin(DefaultUserAdmin):
    def save_model(self, request, obj, form, change):
        if change:  # Si estamos actualizando el usuario
            original_obj = User.objects.get(id=obj.id)
            if obj.is_staff != original_obj.is_staff:  # Si el estado de "is_staff" ha cambiado
                if obj.is_staff:  # Si se ha cambiado a staff
                    staff_group, created = Group.objects.get_or_create(name='Staff_user')
                    if created:  # Si el grupo fue creado, añadimos los permisos
                        # Permisos para Productos
                        product_content_type = ContentType.objects.get(app_label='product', model='productos')
                        product_view_permission = Permission.objects.get(content_type=product_content_type, codename='view_productos')
                        product_add_permission = Permission.objects.get(content_type=product_content_type, codename='add_productos')
                        
                        staff_group.permissions.add(product_view_permission, product_add_permission)
                        
                        # Permisos para Categorías
                        category_content_type = ContentType.objects.get(app_label='product', model='categorias')
                        category_view_permission = Permission.objects.get(content_type=category_content_type, codename='view_categorias')
                        category_add_permission = Permission.objects.get(content_type=category_content_type, codename='add_categorias')
                        
                        staff_group.permissions.add(category_view_permission, category_add_permission)

                        # Permisos para Compras y Ventas
                        purchase_content_type = ContentType.objects.get(app_label='buysSales', model='compras')
                        
                        purchase_view_permission = Permission.objects.get(content_type=purchase_content_type, codename='view_compras')
                        
                        staff_group.permissions.add(purchase_view_permission)


                    # Añadimos el usuario al grupo
                    obj.groups.add(staff_group)
                else:  # Si se ha cambiado a no staff
                    # Eliminamos al usuario del grupo 'Staff'
                    staff_group = Group.objects.get(name='Staff_user')
                    obj.groups.remove(staff_group)

        super().save_model(request, obj, form, change)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


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