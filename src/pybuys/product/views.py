import logging
from django.db.models import Q

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect, render
from django import template
import product
import utils
from product.models import Categorias, Productos

register = template.Library()


def product_detail(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    return render(request, "product/detail.html", {"producto": producto})


def product_new(request):
    return render(request, "product/new.html", {})


def product_edit(request, pk):
    return render(request, "product/edit.html", {})


def product_list(productos):
    return render("product/list.html", {"productos", productos})


def productos(request):
    query = request.GET.get("query", "")
    id_categoria = int(request.GET.get("categoria", 0))
    productos = Productos.objects.filter(cantidad__gt=0)
    if id_categoria:
        productos = list(
            filter(
                lambda producto: utils.pertenece_a_categoria(
                    producto.categoria, Categorias.objects.get(pk=id_categoria)
                ),
                productos,
            )
        )

    elif query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    else:
        return redirect(request, "index")
    return render(
        request,
        "core/index.html",
        {
            "productos": productos,
            "query": query,
            "grupo": id_categoria,
        },
    )


"""
def category(request, pk):
    categoria = Categorias.objects.get(pk=pk)
    productos = Productos.objects.all()
    # filtrar los productos que pertenecen a la categoría
    productos_filtrados = []
    for producto in productos:
        if utils.pertenece_a_categoria(producto.categoria, categoria):
            productos_filtrados.append(producto)
    categorias = Categorias.objects.filter(grupo__isnull=True)
    return render(
        request,
        "product/category.html",
        {
            "productos": productos_filtrados,
            "categorias": categorias,
            "categoria": categoria,
        },
    )
"""
