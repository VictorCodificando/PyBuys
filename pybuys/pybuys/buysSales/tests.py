from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django.core.files.uploadedfile import SimpleUploadedFile

from product.models import Categorias, Productos
from buysSales.models import ProductosEnCarrito, Compras, Ventas
from buysSales.admin import ComprasAdmin


class BuysSalesModelTest(TestCase):
    def setUp(self):
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

    def test_create_productos_en_carrito(self):
        productos_en_carrito = ProductosEnCarrito.objects.create(
            id_usuario=self.user, producto=self.producto, cantidad=5
        )

        self.assertEqual(ProductosEnCarrito.objects.count(), 1)
        self.assertEqual(productos_en_carrito.id_usuario, self.user)
        self.assertEqual(productos_en_carrito.producto, self.producto)
        self.assertEqual(productos_en_carrito.cantidad, 5)

    def test_create_compras(self):
        compra = Compras.objects.create(
            id_usuario=self.user, id_producto=self.producto, cantidad=3
        )

        self.assertEqual(Compras.objects.count(), 1)
        self.assertEqual(compra.id_usuario, self.user)
        self.assertEqual(compra.id_producto, self.producto)
        self.assertEqual(compra.cantidad, 3)

    def test_create_ventas(self):
        venta = Ventas.objects.create(
            id_usuario=self.user, id_producto=self.producto, cantidad=2
        )

        self.assertEqual(Ventas.objects.count(), 1)
        self.assertEqual(venta.id_usuario, self.user)
        self.assertEqual(venta.id_producto, self.producto)
        self.assertEqual(venta.cantidad, 2)


class MockRequest:
    def __init__(self, user=None):
        self.user = user


class ComprasAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = ComprasAdmin(Compras, self.site)

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

        self.compra = Compras.objects.create(
            id_usuario=self.user,
            id_producto=self.producto,
            cantidad=5,
        )

    def test_save_model(self):
        request = MockRequest(user=self.user)
        self.admin.save_model(request, self.compra, None, False)

        compra = Compras.objects.get(id_usuario=self.user, id_producto=self.producto)
        self.assertIsNotNone(compra)
        self.assertEqual(compra.id_usuario, self.user)
