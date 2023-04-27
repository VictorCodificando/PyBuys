from django.db import models

"""

class Categorias(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    grupo = models.ForeignKey("self", on_delete=models.CASCADE, null=True)


class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    foto = models.CharField(max_length=50)
    rebaja = models.FloatField()
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)


class Caracteristicas(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, unique=True)


class CaracteristicaPorProducto(models.Model):
    caracteristica_id = models.ForeignKey(Caracteristicas, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["caracteristica_id", "producto_id"], name="unique_caract_prod"
            ),
        ]


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
"""
