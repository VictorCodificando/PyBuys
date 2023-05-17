import os
import re

from django.core.validators import MinValueValidator
from django.db import models


from pybuys import settings

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
    image = models.ImageField(upload_to="products")
    rebaja = models.FloatField(default=0, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super().delete(*args, **kwargs)

    def get_precio(self):
        precio_con_descuento = self.precio - (self.precio * (self.rebaja/100))
        return round(precio_con_descuento, 2)
    

    def get_precio_real(self):
        return "{:.2f}€".format(self.get_precio())
    
    def get_descripcion_formateada(self):
        # Sustituir '*' por un punto de bala y agregar saltos de línea después de cada punto
        texto = self.descripcion.replace('* ', '• ').replace('.', '.<br>').replace('\n', '<br>')
        # Identificar todo lo que esté dentro de 3 comillas y ponerlo en negrita
        texto = re.sub(r'\'{3}(.*?)\'{3}', r'<br><strong>\1</strong><br>', texto)
        return f'{texto}'
