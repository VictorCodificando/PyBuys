from django import template
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.template.loader import get_template

from product.models import Categorias

register = template.Library()

@register.simple_tag
def show_product_list(productos):
    return {'productos': productos}

product_template = get_template('product/product_list.html')
register.inclusion_tag(product_template)(show_product_list)

@register.simple_tag
def todas_categorias_hijas(id_categoria):
    categorias = Categorias.objects.all()
    if id_categoria == None:
        return categorias.filter(grupo__isnull=True)
    categorias_hijas = []
    for categoria in categorias:
        if (categoria.grupo is not None) and (categoria.grupo.pk == id_categoria):
            categorias_hijas.append(categoria)
    return categorias_hijas