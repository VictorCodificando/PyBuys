from django.apps import AppConfig
from django.db.models import Q

class BuyssalesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "buysSales"

    def ready(self):
        self.create_staff_group()

    @staticmethod
    def create_staff_group():
        from django.contrib.auth.models import User, Group, Permission
        staff_group, created = Group.objects.get_or_create(name='staff_users')

        if created:
            permissions = Permission.objects.filter(Q(codename__in=[
                'view_productos', 'view_categorias', 'view_compras', 'view_productosencarrito',
                'view_ventas', 'add_productos', 'add_categorias', 'change_productos',
                'change_categorias', 'delete_productos', 'delete_categorias']))
            
            staff_group.permissions.set(permissions)
        
        staff_users = User.objects.filter(is_staff=True)
        staff_group.user_set.set(staff_users)
