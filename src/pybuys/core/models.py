from django.db import models

"""


class Cuentas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=64)
    tipo_de_cuenta = models.CharField(
        max_length=50,
        validators=[
            models.RegexValidator(
                regex="^(ADMIN|NORMAL)$",
                message="Tipo de cuenta inválido",
                code="invalid_tipo_de_cuenta",
            )
        ],
    )


class Sesiones(models.Model):
    id = models.AutoField(primary_key=True)
    clave_encriptada = models.CharField(max_length=64)
    usuario_id = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)


class ProductosEnCarrito(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()


class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


accounts: para las páginas de inicio de sesión y creación de cuentas.
core: para la página de inicio (index) y la página de búsqueda.
products: para la página de detalle de producto.
cart: para la gestión del carrito de compras.
purchases: para la administración de las compras.
user_settings: para la configuración de la cuenta de usuario.


app "accounts" con los modelos:
Cuentas
Sesiones
app "products" con los modelos:
Categorias
Productos
Caracteristicas
CaracteristicaPorProducto
app "cart" con los modelos:
ProductosEnCarrito
app "orders" con los modelos:
Compras
Ventas
"""
