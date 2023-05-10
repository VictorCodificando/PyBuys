from django.db import models
from django.contrib.auth.models import User
from product.models import Productos
from django.core.validators import MinValueValidator

class ProductosEnCarrito(models.Model):
    class Meta:
        verbose_name = "Producto en carrito"
        verbose_name_plural = "Productos en carrito"

    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])


class Compras(models.Model):
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.id_usuario} - {self.id_producto} - {self.cantidad} - {self.creado}"
        )


class Ventas(models.Model):
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    creado = models.DateTimeField(auto_now_add=True)
