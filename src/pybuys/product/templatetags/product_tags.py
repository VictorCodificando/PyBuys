# myapp/templatetags/product_tags.py

from django import template
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.template.loader import get_template

register = template.Library()

@register.simple_tag
def show_product_list(productos):
    return {'productos': productos}

product_template = get_template('product/product_list.html')
register.inclusion_tag(product_template)(show_product_list)