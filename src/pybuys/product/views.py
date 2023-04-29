from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django import template
import utils
from product.models import Categorias, Productos

register = template.Library()


def product_detail(request, pk):
    return render(request, "product/detail.html", {})


def product_new(request):
    return render(request, "product/new.html", {})


def product_edit(request, pk):
    return render(request, "product/edit.html", {})


def product_list(productos):
    return render("product/list.html", {"productos", productos})


def category(request, pk):
    categoria = Categorias.objects.get(pk=pk)
    productos = Productos.objects.all()
    # filtrar los productos que pertenecen a la categoría
    productos_filtrados = []
    for producto in productos:
        if utils.pertenece_a_categoria(producto.categoria, categoria):
            productos_filtrados.append(producto)
    return render(request, "product/category.html", {"productos": productos_filtrados})
