from django import template
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from buysSales.models import ProductosEnCarrito
from product.models import Categorias, Productos


register = template.Library()


@register.simple_tag
def show_product_list(productos):
    return {"productos": productos}


product_template = get_template("product/product_list.html")
register.inclusion_tag(product_template)(show_product_list)


@register.simple_tag
def todas_categorias_hijas(id_categoria):
    categorias = Categorias.objects.all()
    if id_categoria is None or id_categoria == "":
        return categorias.filter(grupo__isnull=True)
    else:
        return categorias.filter(grupo__pk=id_categoria)


@register.simple_tag
def obtener_todas_categorias(categoria):
    categoria = get_object_or_404(Categorias, pk=categoria)
    categorias_padre = []
    if categoria is not None:
        categorias_padre.append(categoria)
        while categoria.grupo is not None:
            categoria = categoria.grupo
            categorias_padre.append(categoria)
    categorias_padre.reverse()
    return categorias_padre


@register.simple_tag
def cantidad_producto_en_carrito(id_producto, id_usuario):
    producto = get_object_or_404(Productos, pk=id_producto)
    carrito = ProductosEnCarrito.objects.filter(
        id_usuario=id_usuario, producto=producto
    )
    if carrito.exists():
        return carrito[0].cantidad
    return 0
