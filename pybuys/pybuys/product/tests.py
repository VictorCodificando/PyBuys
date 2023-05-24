import os
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.admin.sites import AdminSite

from product.models import Productos, Categorias
from pybuys import settings
from .models import Productos, Categorias
from product.templatetags.custom_tags import (show_product_list,
                                               todas_categorias_hijas,
                                               obtener_todas_categorias,
                                               cantidad_producto_en_carrito)

from django.test import TestCase
from product.admin import ProductosAdmin
from buysSales.models import ProductosEnCarrito, Compras


# Test modelo
class ProductosModelTest(TestCase):
    def setUp(self):
        self.categoria = Categorias.objects.create(nombre="test_category")
        self.producto = Productos.objects.create(
            nombre="test",
            precio=100,
            image=SimpleUploadedFile(
                name="test_image.jpg", content=b"", content_type="image/jpeg"
            ),
            cantidad=10,
            categoria=self.categoria,
            descripcion="""Esto es una 'descripción' de prueba. Se utilizará para las pruebas unitarias.
            * Esta es una lista
            * Esto es otro elemento de la lista.
            '''
            Esto es una nota adicional en negrita.
            '''
            """,
        )

    # Test del método delete
    def test_delete_method(self):
        image_path = os.path.join(settings.MEDIA_ROOT, self.producto.image.name)
        self.producto.delete()
        self.assertFalse(os.path.exists(image_path))

    def test_delete_sin_imagen(self):
        self.producto.image = None
        self.producto.save()
        self.producto.delete()  # No debe dar error

    # Test del método get_precio
    def test_get_precio_sin_descuento(self):
        self.producto.rebaja = 10
        self.producto.save()
        self.assertEqual(self.producto.get_precio(), 90)

    def test_get_precio_sin_descuento(self):
        self.assertEqual(self.producto.get_precio(), 100)

    def test_get_precio_con_precio_cero(self):
        self.producto.precio = 0
        self.producto.save()
        self.assertEqual(self.producto.get_precio(), 0)

    def test_get_precio_con_descuento_negativo(self):
        self.producto.rebaja = -10
        self.producto.save()
        self.assertEqual(self.producto.get_precio(), 100)  # El descuento no se aplica

    def test_get_precio_con_descuento_mayor_100(self):
        self.producto.rebaja = 110
        self.producto.save()
        self.assertEqual(
            self.producto.get_precio(), 0
        )  # El precio no puede ser negativo

    # Test del método get_precio_real
    def test_get_precio_real(self):
        self.assertEqual(self.producto.get_precio_real(), "100.00€")

    # Test del método get_descripcion_formateada
    def test_get_descripcion_formateada(self):
        formateado = self.producto.get_descripcion_formateada()
        self.assertIn("• ", formateado)
        self.assertIn(".<br>", formateado)
        self.assertIn("<strong>", formateado)
        self.assertIn("</strong>", formateado)
        self.assertNotIn("'''", formateado)


# Test de los custom tags
class TestTemplateTags(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="test1234")

        self.categoria1 = Categorias.objects.create(nombre="Cat 1", grupo=None)
        self.categoria2 = Categorias.objects.create(
            nombre="Cat 2", grupo=self.categoria1
        )

        self.producto1 = Productos.objects.create(
            nombre="Producto 1",
            precio=100.00,
            image=None,
            rebaja=10,
            cantidad=10,
            categoria=self.categoria1,
            descripcion="Descripción del producto",
        )

        self.producto2 = Productos.objects.create(
            nombre="Producto 2",
            precio=200.00,
            image=None,
            rebaja=20,
            cantidad=5,
            categoria=self.categoria2,
            descripcion="Descripción del producto",
        )

        self.carrito = ProductosEnCarrito.objects.create(
            id_usuario=self.user, producto=self.producto1, cantidad=3
        )

    def test_show_product_list(self):
        productos = Productos.objects.all()
        self.assertEqual(show_product_list(productos), {"productos": productos})

    def test_todas_categorias_hijas(self):
        self.assertEqual(
            list(todas_categorias_hijas(self.categoria1.id)), [self.categoria2]
        )
        self.assertEqual(list(todas_categorias_hijas(None)), [self.categoria1])

    def test_obtener_todas_categorias(self):
        self.assertEqual(
            obtener_todas_categorias(self.categoria2.id),
            [self.categoria1, self.categoria2],
        )

    def test_cantidad_producto_en_carrito(self):
        self.assertEqual(
            cantidad_producto_en_carrito(self.producto1.id, self.user.id), 3
        )
        self.assertEqual(
            cantidad_producto_en_carrito(self.producto2.id, self.user.id), 0
        )


class MockRequest:
    def __init__(self, user=None):
        self.user = user


class ProductosAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = ProductosAdmin(Productos, self.site)

        self.user = User.objects.create_user(username="user1", password="test1234")

        self.categoria = Categorias.objects.create(
            nombre="Cat 1",
            grupo=None,
        )

        self.producto = Productos.objects.create(
            nombre="Producto 1",
            precio=100.00,
            image=None,
            rebaja=10,
            cantidad=10,
            categoria=self.categoria,
            descripcion="Descripción del producto",
        )

    def test_save_model(self):
        request = MockRequest(user=self.user)
        self.admin.save_model(request, self.producto, None, False)

        compra = Compras.objects.get(id_usuario=self.user, id_producto=self.producto)
        self.assertIsNotNone(compra)
        self.assertEqual(compra.cantidad, self.producto.cantidad)
