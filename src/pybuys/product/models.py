from django.db import models


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
