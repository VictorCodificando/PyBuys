from django.db import models
import os


class Categorias(models.Model):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"

    nombre = models.CharField(max_length=40)
    grupo = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

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
    descripcion = models.CharField(max_length=600)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        # Eliminar la imagen del producto si existe
        if self.image:
            os.remove(self.image.path)
        # Llamar al método delete() del modelo base para eliminar el objeto
        super().delete(*args, **kwargs)
