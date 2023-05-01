from django import template
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.db.models import Q
from product.models import Categorias, Productos

from django.shortcuts import get_object_or_404

register = template.Library()


@register.simple_tag
def show_product_list(productos):
    return {"productos": productos}


product_template = get_template("product/product_list.html")
register.inclusion_tag(product_template)(show_product_list)


@register.simple_tag
def todas_categorias_hijas(id_categoria):
    categorias = Categorias.objects.all()
    if id_categoria == None or id_categoria == "":
        return categorias.filter(grupo__isnull=True)
    categorias_hijas = []
    for categoria in categorias:
        if (categoria.grupo is not None) and (categoria.grupo.pk == id_categoria):
            categorias_hijas.append(categoria)
    return categorias_hijas

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
