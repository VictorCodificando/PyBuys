from django.db import models


class Categorias(models.Model):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"

    nombre = models.CharField(max_length=40)
    grupo = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre


class Caracteristicas(models.Model):
    class Meta:
        verbose_name = "Caracteristica"
        verbose_name_plural = "Caracteristicas"

    descripcion = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.descripcion


class Productos(models.Model):
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    image = models.ImageField(upload_to="products", blank=True, null=True)
    rebaja = models.FloatField()
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    caracteristicas = models.ManyToManyField(Caracteristicas)
    def __str__(self):
        return self.nombre
